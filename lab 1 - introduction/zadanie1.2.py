from datetime import datetime, timedelta

time_zones = {
    'UTC': 0,
    'CET': 1,
    'CEST': 2,
    'PST': -8,
}

def current_time_in_zone(time_zone):
    if time_zone not in time_zones:
        return "Nieznana strefa czasowa"
    
    offset = time_zones[time_zone]

    current_time_utc = datetime.utcnow()
    current_time_in_zone = current_time_utc + timedelta(hours=offset)
    
    return current_time_in_zone.strftime("%Y-%m-%d %H:%M:%S")

print("Aktualny czas w strefie UTC:", current_time_in_zone('UTC'))
print("Aktualny czas w strefie CET:", current_time_in_zone('CET'))
print("Aktualny czas w strefie CEST:", current_time_in_zone('CEST'))
print("Aktualny czas w strefie PST:", current_time_in_zone('PST'))