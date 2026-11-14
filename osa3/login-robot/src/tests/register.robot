*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  kaisa  kaisa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  kw  kiiwi123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  k4isa  kaisa456
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  nella  nel4
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  karen  karenkaren
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command