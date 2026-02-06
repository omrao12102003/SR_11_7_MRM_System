def basel_traffic_light(breaches, days=250, confidence=0.99):
    """
    Basel Traffic Light Framework (SR 11-7 compatible)
    99% VaR, 250 days:
    GREEN: 0-4 breaches
    YELLOW: 5-9 breaches  
    RED: 10+ breaches
    """
    x = breaches if isinstance(breaches, int) else breaches.sum()
    
    if x <= 4:
        zone = "GREEN"
        action = "Model acceptable"
    elif x <= 9:
        zone = "YELLOW" 
        action = "Review required"
    else:
        zone = "RED"
        action = "Model remediation"
    
    print(f"Basel Traffic Light ({days} days, {confidence*100}% VaR):")
    print(f"Breaches: {x}/{days}")
    print(f"Zone: {zone}")
    print(f"Action: {action}")
    
    return zone, x, action

if __name__ == "__main__":
    print("Test GREEN (3 breaches)")
    basel_traffic_light(3)
    
    print("\nTest YELLOW (7 breaches)")
    basel_traffic_light(7)
    
    print("\nTest RED (12 breaches)")
    basel_traffic_light(12)
