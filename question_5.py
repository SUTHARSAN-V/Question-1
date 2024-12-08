def find_strongest_trainees(strengths):
    for strength in strengths:
        if not (1 <= strength <= 200):
            return "INVALID INPUT"
    
    averages = []
    for i in range(4):
        trainee_strengths = strengths[i::4]
        avg_strength = round(sum(trainee_strengths) / 3)
        averages.append(avg_strength)
    
    highest_avg = max(averages)
    
    if highest_avg < 100:
        return "All trainees are unfit"
    
    strongest_trainees = [
        f"Trainee Number : {i + 1} with Average Strength: {avg}" 
        for i, avg in enumerate(averages) if avg == highest_avg
    ]
    
    return "\n".join(strongest_trainees)

strengths = [int(input()) for _ in range(12)]

result = find_strongest_trainees(strengths)
print(result)
