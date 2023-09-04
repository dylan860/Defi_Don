pragma solidity ^0.5.17;

import "./DFORT_Coin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract Dfort_Corwdsale is Corwdsale , MintedCrowdsale {
    constructor (
        uint rate,
        address payable wallet,
        DFORT_Coin token
    ) public Crowdsale(rate,token,wallet);

}
contract DFORT_Coin_Deployer{
    address public DFORT_COIN_ADDRESS;
    address public DFORT_CROWDSALE_ADDRESS;
    constructor (
        string memory name,
        string memory symbol,
        address payable wallet
    ) public {
        FORT_COIN TOKEN = new DFORT_Coin(name,symbol,0);
        FORT_COIN_ADDRESS =  address(token); 
        FORT_CROWDSALE_ADDRESS = ADDRESS(Dfort_Crowdsale);
        token.addMinter(DFORT_CROWDSALE_ADDRESS);
        token.renounceMinter();    }
}


contract DONFORTUNESTokenDeployer {
    address public DONFORTUNESTokenAddress;

    constructor (
        string memory name,
        string memory symbol,
        uint initial_supply
    ) public {
        DONFORTUNESToken token = new DONFORTUNESToken(name, symbol, initial_supply);
        DONFORTUNESTokenAddress = address(token);
    }
}