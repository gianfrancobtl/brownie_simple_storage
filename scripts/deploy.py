from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # account = accounts.load("gianbattolla-account")
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})


def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add((config["wallets"]["from_key"]))


def main():
    deploy_simple_storage()
