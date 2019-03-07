# Make imports
import socket
import sys

# Welcome message:
print("")      
print("")                                                                     
print("   ▄██████▄   ▄█     █▄     ▄████████         ▄████████  ▄██████▄   ▄████████  ▄█     ▄████████     ███     ▄██   ▄   ")
print("  ███    ███ ███     ███   ███    ███        ███    ███ ███    ███ ███    ███ ███    ███    ███ ▀█████████▄ ███   ██▄")
print("  ███    ███ ███     ███   ███    █▀         ███    █▀  ███    ███ ███    █▀  ███▌   ███    █▀     ▀███▀▀██ ███▄▄▄███ ")
print("  ███    ███ ███     ███   ███               ███        ███    ███ ███        ███▌  ▄███▄▄▄         ███   ▀ ▀▀▀▀▀▀███ ")
print("  ███    ███ ███     ███ ▀███████████      ▀███████████ ███    ███ ███        ███▌ ▀▀███▀▀▀         ███     ▄██   ███ ")
print("  ███    ███ ███     ███          ███               ███ ███    ███ ███    █▄  ███    ███    █▄      ███     ███   ███ ")
print("  ███    ███ ███ ▄█▄ ███    ▄█    ███         ▄█    ███ ███    ███ ███    ███ ███    ███    ███     ███     ███   ███ ")
print("   ▀██████▀   ▀███▀███▀   ▄████████▀        ▄████████▀   ▀██████▀  ████████▀  █▀     ██████████    ▄████▀    ▀█████▀  ")
print(" ")                                                                                    
print("                               FakePortListener coded by OWSSociety | Galletita Oreo")      
print("                                   Visit: https://www.github.com/owssociety/")
print("")

# Read from user input and save as "PORT"
PORT = input("(!) Port >> ")

# Try
try:
	# Make an integer from the (STR) user imput
	bport = int(PORT)
	# Make a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the port in to the socket
	s.bind(('', bport))
	# Show "binding port" message
	print("(!) Binding port: " + PORT)

# Executed on error
except socket.error as msg:
	# Show the error message
	print("(!) Error binding port: " + PORT)
	# Exit from this scripts
	sys.exit()

# Print "Succefully" message
print ('(!) Binding Complete!')
# Listen to in the socket
s.listen(10)
# Print "listening" message
print ('(!) Socket now listening')

# Make a loop
while 1:
	# Get connection data when is pinged
    conn, addr = s.accept()
    # Print who is pinged to the fake port
    print ('(!) New Request in: ' + addr[0] + ':' + str(addr[1]))

# Close socket
s.close()