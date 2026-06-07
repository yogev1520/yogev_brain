from brain.process_command import process_command
from brain.memory import load_memory

print("=== TEST 1 ===")
print(process_command("מה מזג האוויר בתל אביב?"))

print("\n=== TEST 2 (חוזר) ===")
print(process_command("מה מזג האוויר בתל אביב?"))

print("\n=== MEMORY ===")
print(load_memory())