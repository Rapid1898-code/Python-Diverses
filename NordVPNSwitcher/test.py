from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

# # rotate trough list of countries
# instructions = initialize_VPN(area_input=['Belgium,France,Netherlands']) # <-- Be aware: the area_input parameter expects a list, not a string
# for i in range(3):
#     rotate_VPN(instructions) #refer to the instructions variable here
#     print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
#     time.sleep(10)

instructions = initialize_VPN(area_input=['random countries europe 8'])
for i in range(3):
    rotate_VPN(instructions) #refer to the instructions variable here
    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
    time.sleep(10)