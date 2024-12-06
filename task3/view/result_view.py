def display_results(event_name, results):
    output = f"Results for {event_name}:\n"
    for participant, score in results:
        output += f"{participant.name}: {score}\n"
    return output
