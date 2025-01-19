import hashlib

class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", "2025-01-19")

    def add_block(self, data, timestamp):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data, timestamp)
        self.chain.append(new_block)

# Example usage
blockchain = Blockchain()
blockchain.add_block("Transaction 1", "2025-01-19")
blockchain.add_block("Transaction 2", "2025-01-20")

for block in blockchain.chain:
    print(f"Block {block.index} | Hash: {block.hash} | Data: {block.data}")
