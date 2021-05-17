from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

# # rotate trough list of countries
# instructions = initialize_VPN(area_input=['Belgium,France,Netherlands']) # <-- Be aware: the area_input parameter expects a list, not a string
# for i in range(3):
#     rotate_VPN(instructions) #refer to the instructions variable here
#     print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
#     time.sleep(10)

# [3] of course, you can try one of the built-in randomizers if you can't be bothered with selecting specific regions
# The following options are avilable:
# random countries X
# random countries europe X
# random countries americas X
# random countries africa east india X
# random countries asia pacific X
# random regions australia X
# random regions canada X
# random regions germany X
# random regions india X
# random regions united states X
instructions = initialize_VPN(area_input=['random countries europe 8'])
for i in range(3):
    rotate_VPN(instructions) #refer to the instructions variable here
    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
    time.sleep(10)

# the following code will perform an infinite loop of picking a random server every hour
instructions = initialize_VPN(area_input=['complete rotation'])
while True:
    rotate_VPN(instructions)
    time.sleep(3600)    