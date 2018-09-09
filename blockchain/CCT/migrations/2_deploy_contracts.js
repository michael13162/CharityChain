var CCT = artifacts.require("./CCT.sol");
var CCTInterface = artifacts.require("./CCTInterface.sol");
var CCTFactory = artifacts.require("./CCTFactory.sol");

module.exports = function(deployer) {
  deployer.deploy(CCTInterface);
  deployer.link(CCTInterface, CCT);
  deployer.deploy(CCT);
  deployer.link(CCTFactory, CCT);
  deployer.deploy(CCTFactory);
};
