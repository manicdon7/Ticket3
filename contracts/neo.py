from web3 import Web3

# Replace this with the NeoLine RPC server URL
rpc_url = "https://rpc.neoline.io/mainnet"

# Connect to the NeoLine RPC server
web3 = Web3(Web3.HTTPProvider(rpc_url))

if web3.isConnected():
    print("Connected to NeoLine RPC server")

    # Example address from your NeoLine wallet
    wallet_address = "your_wallet_address_here"

    # Example contract address and ABI
    contract_address = "contract_address_here"
    contract_abi = [
        # Contract ABI here
    ]

    # Instantiate the contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Example function call
    function_name = "function_name_here"
    function_params = [web3.toWei(1, "ether")]

    # Unlock NeoLine wallet for signing transactions
    web3.middleware_onion.inject(web3.middleware.geth_poa_middleware, layer=0)
    web3.middleware_onion.add(
        Web3.Web3Debugging.geth_poa_middleware,
        {"gas_limit": 5000000, "chainId": 1},
    )

    # Build and sign the transaction
    transaction = contract.functions[function_name](*function_params).buildTransaction(
        {
            "chainId": 1,
            "gas": 2000000,
            "gasPrice": web3.toWei("20", "gwei"),
            "nonce": web3.eth.getTransactionCount(wallet_address),
        }
    )

    signed_transaction = web3.eth.account.signTransaction(
        transaction, private_key="your_private_key_here"
    )

    # Send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    print("Transaction sent. Transaction hash:", web3.toHex(tx_hash))

else:
    print("Failed to connect to NeoLine RPC server")
