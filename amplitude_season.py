

#Test cases for testing
T= [-3, -14, -5, 7, 8, 42, 8,3]
T= [2,-3,3,1,10,8,2,5,13,-5,3,-18]

# Code to find the max amplitude
winter = T[0:int(num_of_days)]
spring = T[int(num_of_days):int(num_of_days*2)]
summer = T[int(num_of_days*2):int(num_of_days*3)]
autumn = T[int(num_of_days*3):int(num_of_days*4)]
winter_diff = abs(max(winter) -min(winter))
spring_diff = abs(max(spring) -min(spring))
summer_diff = abs(max(summer) -min(summer))
autumn_diff = abs(max(autumn) -min(autumn))
season_list = [ "WINTER", "SPRING", "SUMMER", "AUTUMN" ]
season_amplitude = [winter_diff,spring_diff,summer_diff,autumn_diff]
print(season_amplitude)
max_value = max(season_amplitude)
max_index = season_amplitude.index(max_value)
print(season_list[max_index])
