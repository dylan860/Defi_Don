import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


# Cache the contracts on load
@st.cache(allow_output_mutation=True)

# Define the load_contract_crowdsales function
def load_contract_crowdsales():
    # Load Art Gallery ABI
    with open(Path("DFORT_Crowdsales_abi.json")) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_Crowdsales")
    # Get the contract
    contract = w3.eth.contract(address=contract_address, abi=certificate_abi)
    # Return the contract from the function
    return contract


# Define the load_contract_coin function
def load_contract_coin():
    # Load Art Gallery ABI
    with open(Path("DFORT_Coin_abi.json")) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_Coin")
    # Get the contract
    contract = w3.eth.contract(address=contract_address, abi=certificate_abi)
    # Return the contract from the function
    return contract


# Define the load_contract_nft function
def load_contract_nft():
    # Load Art Gallery ABI
    with open(Path("NFTabi.json")) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_NFT")
    # Get the contract
    contract = w3.eth.contract(address=contract_address, abi=certificate_abi)
    # Return the contract from the function
    return contract


# Load the contracts
try:
    contract_crowdsales = load_contract_crowdsales()
    contract_coin = load_contract_coin()
    contract_nft = load_contract_nft()
except:
    pass

# Define the accounts
try:
    accounts = w3.eth.accounts
    account = accounts[0]
except:
    accounts = [
        "0xc07C2147eA6609BE2fdF00d1d1643C6709DcA23c",
        "0x808bc3b16f55aA40447929fCa22CA807855c243B",
        "0x5aA6f3415502B768241F71F8B4c7a2Aa419Af7ED",
    ]

##########################################################################################

# Streamlit UI

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "The Dons",
        "Future Don",
        "Don Smart",
        "Buy Fortunes",
        "NFT Dons",
        "Business",
        "Newsletter",
    ]
)

with tab2:
    st.header("Defi Don")
    st.markdown(
        """
        Having Created a trading bot algorithm, our future revolves around creating a versatile coin designed for trading, holding, and staking. We place paramount importance on executing our objectives with unwavering integrity and fostering transparent relationships with our valued customers.
        
        To generate revenue, DeFi Don will charge fees for its services. These fees will be paid in the DeFi Don native token, which will be used to incentivize users to participate in the protocol and to secure the network.
        The business model of DeFi Don is still in its early stages, but it has the potential to be a major player in the decentralized finance industry. By offering a variety of financial services to businesses, DeFi Don can help to make decentralized finance more accessible and efficient.\n

    
        We will connect the algorithm to a blockchain and track the results, we will use a combination of smart contracts and APIs.
        Smart contracts are self-executing contracts with the terms of the agreement directly written into code on the blockchain.
        We will design and deploy a smart contract that interfaces with the algorithm.
        The algorithm can then perform its computations and produce results, which are stored and updated on the blockchain through the smart contract.
        By utilizing APIs, we can create a connection between the algorithm and the smart contract.
        This allows the algorithm to interact with the blockchain, sending data to the smart contract and retrieving results or information from it.

        Here is a simple diagram \n
        Algorithm \n
        <-> \n
        Smart Contract <-> API <-> Blockchain \n
        <-> \n
        Results Tracking \n
        The algorithm communicates with the smart contract through an API, which in turn interacts with the blockchain.
        This enables the algorithm to push data to the smart contract and retrieve results from it, facilitating the tracking of outcomes on the blockchain. 

         """
    )

with tab1:
    st.header("Don Fortunes Team")
    st.markdown(
        """
        Pinda Johnson \n
        Dylan Brown \n
        Branzil Engracia \n
            
        We proudly represent a vibrant and multifaceted collective comprising individuals who are not only 
        ardent aficionados of technology and blockchain but also visionary entrepreneurs. \n

        Our unified mission revolves around the provision of an unparalleled blend of convenience and 
        profitability within the realm of digital currency investment, catering to a broad spectrum of clients. 
        Through our unwavering dedication, extensive expertise, and fervent passion for cutting-edge advancements, 
        we strive to usher in a new era of financial empowerment, ensuring that every client, regardless of background or 
        experience, can seamlessly partake in the transformative potential of digital currencies.
        """
    )
    st.image("coin_logo.png", width=500)

with tab4:
    st.header("Buy Fortunes")
    selected_account_1 = st.selectbox("Select Account to Buy", options=accounts)
    fortunes_to_buy = st.number_input("How much Fortunes Do you want to purchase?")

    if st.button("Purchase Fortunes"):
        st.code(
            "contract_crowdsales.functions.buyFortunes(selected_account).transact({'from': selected_account, 'gas': 1000000})"
        )
        st.balloons()
    st.markdown(
        """
        Introducing Defi_Don's Fortune Token:
        - With a fixed supply of 21 million tokens, Fortunes Token offers scarcity and value.
        - Built as an ERC20 token, it seamlessly interfaces with other ERC20 tokens and serves various functions within the realm of DeFi applications.
        - Precisely divided into 18 decimals, the token's granularity enables transactions at even the tiniest scales.
        - Facilitating fluidity, DONFORTUNESToken can be freely traded on decentralized exchanges, facilitating buying and selling activities.
        - The responsibility of minting new tokens rests with the DFORT_Crowdsale contract, a standard and secure means of issuing tokens.
        - Empowering participation, the DFORT_Crowdsale contract enables individuals to contribute ETH in exchange for Fortunes Token.

        """
    )

with tab5:
    st.header("Stake Fortunes")
    selected_account_2 = st.selectbox("Select Account to Stake", options=accounts)
    fortunes_to_stake = st.number_input(
        "How much Fortunes Do you want to Stake with us?"
    )

    if st.button("Stake Fortunes"):
        st.code(
            "contract_coin.functions.stakeFortunes(selected_account).transact({'from': selected_account, 'gas': 1000000})"
        )
        st.balloons()
    st.markdown(
        """
            DeFi Don could raise capital from Prop Trading Firms by sharing the performance of its results. 
            This means that Prop Trading Firms would invest in DeFi Don and then share in the profits that the company generates. This is a common way for DeFi Protocols to raise capital. \n
            
            """
    )


with tab6:
    st.header("Don Business")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    st.markdown(
        """
        DeFi Don could also partner with real estate protocols such as Hom Dao. This would allow DeFi Don to offer its services to real estate investors and developers. For example, DeFi Don could help real estate investors to secure financing for their projects or to manage their investments. \n
        DeFi Don could also build farming protocols that support payments to farmers and payments back to the protocol utilizing carbon credits to supplement funding. This would allow DeFi Don to support sustainable agriculture and to help farmers to earn a fair price for their crops. \n
        Investment groups, condo associations, developers, and other such organizations could use DeFi Don's protocols to manage their finances and to access liquidity. For example, an investment group could use DeFi Don's lending and borrowing services to raise capital for its investments. \n
        Overall, the business model of DeFi Don is  to offer a suite of DeFi services to businesses and accredited investors. These services could help businesses to manage their finances, to access liquidity, and to earn yield on their assets. \n
        The possibilities are endless. The important thing is to choose a business model that is right for you and your team, and that you are passionate about. \n

        """
    )

    st.markdown(
        """
        Here are some of the challenges that DeFi Don may face:
        - Regulatory uncertainty: The regulatory landscape for DeFi is still evolving, and this could pose a challenge to DeFi Don's business.
        - Security: DeFi protocols are vulnerable to hacks and other security breaches. DeFi Don will need to take steps to mitigate these risks.
        - Adoption: DeFi is still a relatively new technology, and it may take some time for businesses to adopt it.
        Despite these challenges, DeFi Don has the potential to be a successful business. By addressing the challenges head-on and providing a valuable service to businesses, DeFi Don can help to shape the future of decentralized finance.
        You could also consider partnering with other DeFi protocols to offer a wider range of services. For example, you could partner with a lending protocol to offer loans to businesses, or with a derivatives protocol to offer hedging products.



        """
    )

with tab7:
    st.header("Newsletter")
    st.text_input("Enter your email address below for updates!")

with tab3:

    def embed_gist(gist_url, width=600, height=400):
        st.markdown(
            f'<iframe src="{gist_url}.pibb" width="{width}" height="{height}"></iframe>',
            unsafe_allow_html=True,  # This is required to embed the HTML iframe
        )

    gist_url_1 = "https://gist.github.com/branztg/84520bec94ba5d226400a36e92b1e709"
    st.write("Crowdsale Smart Contract:")
    embed_gist(gist_url_1)

    gist_url_2 = "https://gist.github.com/branztg/e733ffc504aba2f786e76ff657895f69"
    st.write("DFORT Coin Smart Contract:")
    embed_gist(gist_url_2)

    gist_url_3 = "https://gist.github.com/branztg/dad46f25becd6422db9200c8b5288725"
    st.write("NFT Smart Contract:")
    embed_gist(gist_url_3)

    gist_url_4 = "https://gist.github.com/branztg/898908ac7821ea939cb6327a096f49b9"
    st.write("Front End Application Code:")
    embed_gist(gist_url_4)
