var CCT = artifacts.require("./CCT.sol");
var CCTInterface = artifacts.require("./CCTInterface.sol");
var CCTFactory = artifacts.require("./CCTFactory.sol");

module.exports = function(deployer) {
  deployer.deploy(CCT, 1000000, "Igor Durovic", 1, "CCT");
};
