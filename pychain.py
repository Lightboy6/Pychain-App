# Blockchain Application
################################################################################
# In this activity, you’ll build a Streamlit application that can both generate
# new blocks of user data and add them to a Python blockchain.

# You will need to complete the following steps:
# 1. Review the starter code included for both the `Block` data class and the
# Streamlit application.
# 2. Modify the "Add Block" button below to add new blocks to the blockchain.
# 3. Display the blockchain data.
# 4. Test the application.
################################################################################
# Imports
import streamlit as st
import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import datetime as datetime
import hashlib

################################################################################
# Step 1:
# Review the provided code in the `app.py` file for both the `Block` data class
# and the Streamlit web application. This mirrors what you created in a prior
# activity.

################################################################################
# Creates the Block and PyChain data classes


@dataclass
class Block:
    vehicle_vin: int
    service_tech: Any
    odometer: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        vehicle_vin = str(self.vehicle_vin).encode()
        sha.update(vehicle_vin)

        service_tech = str(self.service_tech).encode()
        sha.update(service_tech)

        odometer = str(self.odometer).encode()
        sha.update(odometer)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Create the data class PyChain


@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(vehicle_vin="", service_tech= "", odometer="" )])


pychain = setup()

st.markdown("# Show me the BLOCKFAX")
st.markdown("## Store car data on a blockchain")

input_odometer_reading = st.text_input("Odometer Reading")
input_service_tech = st.text_input("Service Technician")
input_vehicle_vin = st.text_input("Vehicle Vin")


################################################################################
# Step 2:
# Modify the Streamlit “Add Block” button code so that when someone clicks the
# button, the code adds a new block to the blockchain.

# Include the following steps:
# 1. Select the previous block in the chain by using the following
# code:`prev_block = pychain.chain[-1]`.
# 2. Hash the previous block by using the following
# code: `prev_block_hash = prev_block.hash_block()`.
# 3. Create a new block by using the following
# code: `new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)`
# 4. Add the new block to the chain by using the following
# code: `pychain.add_block(new_block)`.

if st.button("Add Block"):

    # @TODO:
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # @TODO:
    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()

    # @TODO:
    # Create a new block in the chain
    new_block = Block(vehicle_vin= input_vehicle_vin, odometer=input_odometer_reading, service_tech=input_service_tech, prev_hash=prev_block_hash)

    # @TODO:
    # Add the new block to the chain
    pychain.add_block(new_block)

################################################################################
# Step 3:
# Display the the `PyChain` ledger data on the Streamlit webpage
# 1. Create a Pandas DataFrame so that the block data will display in a more user-friendly manner. To do so, use the following
# code: `pychain_df = pd.DataFrame(pychain.chain)`
# 2. Write the Pandas DataFrame to the screen by using the `st.write` function.


st.markdown("## PyChain Ledger")

# @TODO:
# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain)

# @TODO:
# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)

################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 3. Adjust the input text in the text box, and then click the Add Block button.
# 4. Review the changes in the `PyChain` ledger that the Streamlit application
# webpage reflects.

################################################################################
