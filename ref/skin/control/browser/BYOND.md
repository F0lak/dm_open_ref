
## BYOND (info)
***
The BYOND object is a built-in shortcut for interacting with the client via JavaScript in a browser control. It contains the following methods:

Performs a <a href="#/{skin}/control/browser/winset">winset</a>, where `id` is the ID of the control to change (or null for global settings), and `params` is an object with parameter,value pairs such as `{"text-color": "red"}`. Parameters can use camelCase, where a capital letter indicates where a hyphen would normally go, e.g. `"textColor"` and `"text-color"` are the same.


```dm

// uncheck a button from JavaScript
BYOND.winset("inventory_button", {isChecked: false});

```


Sends a <a href="#/{skin}/control/browser/winset">winget</a>, where `id` is the ID of the control to retrieve (or null for global settings), and `props` is a single property or an array of properties to retrieve. As with `winset`, camelCase is allowed, but the result will not use camelCase.

Returns a Promise object, so this call can be used with the `await` keyword or followed by `then()`. The result inside the promise is an object with parameter,value pairs, such as `{"background-color": {value: "#ff0000", red: 255, green: 0, blue: 0, isDefault: false}}`.


```dm

// get a button's status JavaScript
let buttonData = await BYOND.winget("inventory_button", "isChecked");
if(buttonData["is-checked"]) {
    alert("The button is checked!");
}

```


Initiates a <a href="#/{skin}/commands">client command</a>. This is basically just a shortcut for using `winset` to run a command.


```dm

// play a sound
BYOND.command(".sound 'ding.ogg'");

```

***