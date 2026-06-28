from modules.analytics import SessionAnalytics


analytics = SessionAnalytics()

print("=" * 45)
print("      AUDIENCE SESSION REPORT")
print("=" * 45)

print(f"Session File          : {analytics.session_file()}")
print(f"Session Duration      : {analytics.session_duration()}")
print(f"People Detected       : {analytics.people_count()}")
print(f"Average Attention     : {analytics.average_attention()}%")
print(f"Average Engagement    : {analytics.average_engagement()}%")
print(f"Highest Engagement    : {analytics.highest_engagement()}%")
print(f"Lowest Engagement     : {analytics.lowest_engagement()}%")
print(f"Average Blink Count   : {analytics.average_blinks()}")
print(f"Most Attentive Person : ID {analytics.most_attentive_person()}")
print(f"Least Attentive Person: ID {analytics.least_attentive_person()}")

print("=" * 45)