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
    with open(Path('DFORT_Crowdsales_abi.json')) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_Crowdsales")
    # Get the contract
    contract = w3.eth.contract(address=contract_address,abi=certificate_abi)
    # Return the contract from the function
    return contract

# Define the load_contract_coin function
def load_contract_coin():
    # Load Art Gallery ABI
    with open(Path('DFORT_Coin_abi.json')) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_Coin")
    # Get the contract
    contract = w3.eth.contract(address=contract_address,abi=certificate_abi)
    # Return the contract from the function
    return contract

# Define the load_contract_nft function
def load_contract_nft():
    # Load Art Gallery ABI
    with open(Path('NFTabi.json')) as f:
        certificate_abi = json.load(f)
    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_DFORT_NFT")
    # Get the contract
    contract = w3.eth.contract(address=contract_address,abi=certificate_abi)
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
["About us","Team","Buy Fortunes","Stake Fortunes","Roadmap","Newsletter","Analytics",])

with tab1:
    st.header("Defi Don")
    st.markdown(
        """
        Empowering Cryptocurrency with Fortunes
        Defi Don stands as a decentralized cryptocurrency platform, underpinned by the "Fortunes" coin. Our mission revolves around creating a versatile coin designed for trading, holding, and staking. We place paramount importance on executing our objectives with unwavering integrity and fostering transparent relationships with our valued investors.
        Outlined below are key facets encapsulating our vision:
        1. **Decentralized Coin**: We are committed to the ideology of decentralization, ensuring that the Fortunes coin remains free from the control of any singular entity.
        2. **Performance-Tied Token**: The Fortunes coin is intrinsically linked to the performance of our exclusive trading bot, known as "Pindabot". This linkage translates into investor rewards that dynamically adjust based on the bot's efficacy.
        3. **Utility in E-Commerce**: The Fortunes coin doubles as a means to purchase goods and services on our web-based platform, amplifying its utility and integration within the broader digital ecosystem.
        4. **Democratic Decision-Making**: Our coin also serves as a tool for democratic participation. Investors can wield their Fortunes tokens to influence pivotal decisions concerning the platform's development trajectory.
        At Defi Don, we're not just crafting a cryptocurrency; we're architecting a resilient financial instrument with a multifaceted purpose. Our commitment to transparency, decentralization, and innovation propels us toward a future where the Fortunes coin becomes an embodiment of empowerment and inclusion.
         """
    )

with tab2:
    st.header("Don Fortunes Team")
    st.markdown(
        """
        Pinda Johnson \n
        Dylan Brown \n
        Branzil Engracia \n
            
        We proudly represent a vibrant and multifaceted collective comprising individuals who are not only 
        ardent aficionados of technology and blockchain but also visionary entrepreneurs. 
        Our unified mission revolves around the provision of an unparalleled blend of convenience and 
        profitability within the realm of digital currency investment, catering to a broad spectrum of investors. 
        Through our unwavering dedication, extensive expertise, and fervent passion for cutting-edge advancements, 
        we strive to usher in a new era of financial empowerment, ensuring that every investor, regardless of background or 
        experience, can seamlessly partake in the transformative potential of digital currencies.
        """
    )
    st.image("coin_logo.png", width=500)

with tab3:
    st.header("Buy Fortunes")
    selected_account_1 = st.selectbox("Select Account to Buy", options=accounts)
    fortunes_to_buy = st.number_input("How much Fortunes Do you want to purchase?")

    if st.button("Purchase Fortunes"):
        st.code("contract_crowdsales.functions.buyFortunes(selected_account).transact({'from': selected_account, 'gas': 1000000})")
        st.balloons()

with tab4:
    st.header("Stake Fortunes")
    selected_account_2 = st.selectbox("Select Account to Stake", options=accounts)
    fortunes_to_stake = st.number_input("How much Fortunes Do you want to Stake with us?")
    st.write(
        """
        At DeFi Don, we pride ourselves on utilizing a unique and proprietary trading strategy
        that has been carefully crafted and refined over time. Our advanced trading bot, 
        which is the result of extensive research and development, 
        is engineered to maximize profitability. 
        This bot continuously scans and trades across multiple markets, 
        ensuring that we take advantage of the best opportunities throughout the entire year. 
        Our commitment to this approach allows us to consistently stay ahead in the dynamic world of 
        decentralized finance, delivering optimal returns for our stakeholders
        """
    )

    if st.button("Stake Fortunes"):
        st.code("contract_coin.functions.stakeFortunes(selected_account).transact({'from': selected_account, 'gas': 1000000})")
        st.balloons()

with tab5:
    st.header("Roadmap")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab6:
    st.header("Newsletter")
    st.text_input("Enter your email address below for updates!")

with tab7:
    st.header("Analytics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Price", "$20356", "$19655")
    col2.metric("Market Cap", "$508,797", "$508,766")
    col3.metric("Volume", "$12,804", "$12,809")
    col4.metric("Circulating Supply", "19,523")