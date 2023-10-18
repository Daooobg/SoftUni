from collections import deque

daily_food = list(map(int, input().split(', ')))
all_stamina = deque(map(int, input().split(', ')))

mountains = deque((('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)))

climbed_peaks = []

for day in range(1, 8):
    if not mountains:
        break

    curr_food = daily_food.pop()
    curr_stamina = all_stamina.popleft()

    energy = curr_stamina + curr_food

    if energy >= mountains[0][1]:
        curr_mountain_info = mountains.popleft()
        climbed_peaks.append(curr_mountain_info[0])

if len(climbed_peaks) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if climbed_peaks:
    print('Conquered peaks:')
    [print(climbed_peak) for climbed_peak in climbed_peaks]