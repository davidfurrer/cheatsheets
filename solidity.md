# Solidity

online editor: https://remix.ethereum.org/

## Hello World with update function

```javascript
pragma solidity 0.5.12;

contract HelloWorld{
    string public message = "Hello World";

    function getMessage() public view returns(string memory){
        return message;
    }

    function setMessage(string memory newMessage) public{
        message = newMessage;
    }
}
```
