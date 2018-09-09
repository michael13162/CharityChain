const CCTFactory =
  artifacts.require('./CCTFactory.sol');

module.exports = (deployer) => {
  deployer.deploy(CCTFactory, { gas: 1000000 });
};
