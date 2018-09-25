arrow_head_width=0
arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))
while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))


print('')
# Draw arrow base (height = 3, width = 2)
ab='*'*arrow_base_width
for i in range(0,arrow_base_height):
    print(ab)

# Draw arrow head (width = 4)
for count in range(arrow_head_width,0,-1):
        print(('*'*count))
