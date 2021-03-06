# fortigaterepr

NOTE:  This should be considered ALPHA!

Built off of Fortinet's fortiosapi library to provide an abstraction and representation of various operational state data of a Fortigate Device.  Currently most operational data is modeled in a sub-classed Pandas Dataframe, and the Dataframe itself can be manipulated like any other Dataframe for manipulation of the output.  Has some helper methods that more or less wrap some of the methods in the fortiosapi library -- most (all?) of the parameters that library accepts are passed through from the FortigateDevice Class, with the same defaults.  The data is sub-classed to allow for some helper methods to clean up the data and also to provide some canned output filtering options like removing certain often-unnecessary columns from printouts, etc.

To gather data from the device, use one of the 'get' methods available such as `get_interfaces()`.  This returns the result and also stores the result as a property of the class instance - i.e. `dev.interfaces`

In general all of the data returned from the device API is stored in the DataFrame, though there is some data cleanup that can occur (i.e. converting epoch timestamp to readable date/time, replacing NaNs with "None" or "N/A", etc.).  Often the number of columns is quite large, and much of the data is not useful most of the time, so each DataFrame has a `get()` method that will return a copy of the DataFrame with certain columns removed (depends upon the table).  If the full DataFrame is needed, you can just reference the appropriate class instance property - i.e. `dev.interfaces`

## Prerequisites

To use the Fortigate REST API, the device must have a defined REST API admin account, with appropriate permissions.  In the GUI you can create an Admin Profile for the REST API admin account under System --> Admin Profiles --> Create New.  From there you can specify what permissions to give for the various sections.  Next, you create a REST API admin account -- in the GUI via System --> Administrators --> Create New --> REST API Admin.  Once you create the API Token you'll have to save it somewhere safe!

Example CLI config:

```bash
config system accprofile
    edit "API_ADMIN_PROFILE"
        set comments "Admin Profile for REST API Access"
        set secfabgrp read-write
        set ftviewgrp read-write
        set authgrp read-write
        set sysgrp read-write
        set netgrp read-write
        set loggrp read-write
        set fwgrp read-write
        set vpngrp read-write
        set utmgrp read-write
        set wifi read-write
    next
end
# create API User:
config system api-user
    edit "apiuser"
        set comments "rest api user"
        set api-key ENC API-TOKEN-ENCRYPTED-STRING-HERE
        set accprofile "API_ADMIN_PROFILE"
        set vdom "root"
        set cors-allow-origin "https://fndn.fortinet.net" ## Allows API exploration with FNDN
        config trusthost
            edit 1
                set ipv4-trusthost 192.168.1.0 255.255.255.0
            next
        end
    next
end
```

### Creating an Admin Profile for API Accounts

fortigaterepr offers some helpful methods to bootstrap creation of admin profiles and rest API users.  It currently supports creating basic read only or read-write admin profiles.  More granular permissions are possible, but are expected to be implemented outside of this library at this time.  The custom profile can be specified when creating the API User if needed.  Below is example of using fortigaterepr to create read only and readwrite profiles.  The `create_admin_profile()` function returns the name of the profile upon success.

```python
from fortigaterepr.fortigaterepr import FortigateDevice
# create device:
dev = FortigateDevice("192.0.2.50", username="username", password="password", verify=False)
# below will return the default RO profile name "API_RO_PROFILE"
ro_profile_name = dev.create_admin_profile(profile_type="RO")

# below will return the custom RW profile name "test_rw_profile"
rw_profile_name = dev.create_admin_profile(profile_type="RW", profile_name="test_rw_profile")
```

### Creating an API User

In cases where an existing API User does not exist, and / or API token not known, the library has a helper method that will create an api user via SSH and create its token, and return that token to the caller, which can then be saved or used as needed for future API calls.  A short example that creates a RO and RW api user (based on profiles created above):

```python
dev = FortigateDevice("192.0.2.50", username="username", password="password", verify=False)

# create a read only api account, and store its api key that is generated
ro_apikey = dev.create_api_user(
    "ro-devapi",
    profile_name=ro_profile_name,
    trusted_hosts_ipv4=["192.168.1.0/24",
    "172.16.1.0/24"],
    comment="Test API User")
# associate api key to device, and get some data
dev.apitoken = ro_apikey
vpns = dev.get_active_ipsec_vpns()
```

## Basic Use

Simple example usage assuming API User and token already exists:

```python
from fortigaterepr.fortigaterepr import FortigateDevice
dev = FortigateDevice(
    "192.0.2.50",
    username="username",
    password="password",
    apitoken="secretapitoken",
    verify=False,
)

if not dev.restapilogin():
    print("Error authenticating to API - exiting!")
    sys.exit(1)

interface_data = dev.get_interfaces()

# print entire interface_data DataFrame:
print(interface_data)

# print a generally more useful subset:
print(interface_data.get())
```

## TODO

* Unit Tests
* Documentation
* more state data gathering / representation
  * Address Book Objects
  * how to add route table size?  as own dataframe, or somehow as part of Route Table DataFrame?
* methods for other output formats -- i.e. a `to_html()` or `to_json()` method that takes all the stored data and writes it to HTML or JSON stdout or to a file.
* add type hints
* Improve dataframe return parsing for handling columns not existing in dataframe
* other?
