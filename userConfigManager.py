'''User Configuration Manager 
- manage their settings such as theme, language, and notifications
- implement functions to add, update, delete, and view user settings'''

# For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
test_settings = {
    'brightness':'low',
    'colour': 'pink',
    'theme':'park',
    'mouse speed' : '2 mouse power',
}

#You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair
def add_setting(settings_dict,kv_pair):
    # Convert the key and value to lowercase.
    new_kvp = []
    for i in kv_pair:
        new_kvp.append(i.lower())
    key = new_kvp[0]
    value = new_kvp[1]
    # If the key setting exists, return message
    if key in settings_dict.keys():
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    # If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return message
    else:
        settings_dict.update({key:value})
        return(f"Setting '{key}' added with value '{value}' successfully!")


print('\nadd_setting TEST 1\n',add_setting(test_settings, ('volume', 'QuiEt aS a MoUse')))

print('\nadd_setting TEST 2\n',add_setting({'theme': 'light'}, ('volume', 'high')))

print('\nadd_setting TEST 3\n',add_setting({'theme': 'light'}, ('THEME', 'dark')))


#You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

def update_setting(settings_dict,kv_pair):
    #Convert the key and value to lowercase.
    new_kvp = []
    for i in kv_pair:
        new_kvp.append(i.lower())
    key = new_kvp[0]
    value = new_kvp[1]
    # If the key setting exists, update its value in the given dictionary of settings and return: message
    if key in settings_dict.keys():
        settings_dict.update({key : value})
        return(f"Setting '{key}' updated to '{value}' successfully!")
    #If the key setting doesn't exist, return message
    # The messages returned should have the key and value in lowercase.
    else:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
    
print('\nupdate_setting TEST 4\n',update_setting({'theme': 'light'}, ('theme', 'dark')))

print('\nupdate_setting TEST 5\n',update_setting({'theme': 'light'}, ('volume', 'high')))

# You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.
def delete_setting(settings_dict,init_key):
    # Convert the key passed to lowercase.
    key = str(init_key).lower()
    # If the key setting exists, remove the key-value pair from the given dictionary of settings and return
    if key in settings_dict.keys():
        del settings_dict[key]
        return(f"Setting '{key}' deleted successfully!")
    # If the key setting does not exist, return message
    # The messages returned should have the key in lowercase.
    else:
        return(f"Setting not found!")

print('\ndelete_setting TEST 5\n',delete_setting(test_settings, ('brightness', 'low')))

print('\ndelete_setting TEST 6\n',delete_setting({'theme': 'light'}, 'theme'))

# You should define a function named view_settings with one parameter representing a dictionary of settings.


def view_settings(settings_dict):
    #Return No settings available. if the given dictionary of settings is empty.
    if not settings_dict:
        return("No settings available.")
    #If the dictionary contains any settings, return a string displaying the settings. 
    #The string should start with Current User Settings: 
    #followed by the key-value pairs, each on a new line and with the key capitalized.
    else:
        new_settings = "Current User Settings:\n"
        for key, value in settings_dict.items():
            setting = f"{key.capitalize()}: {value.lower()}\n"
            new_settings += setting
        return(new_settings)

print('\nview_setting TEST 7\n',view_settings(test_settings))
print('\nview_setting TEST 8\n',view_settings({'theme': 'light'}))
print('\nview_setting TEST 9\n',repr(view_settings({})))

