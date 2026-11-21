def change_due(paid, bill):
    """Return the change owed."""
 
    if paid < bill:
        raise ValueError(
            f"Paid {paid} but the bill is {bill}")
 
    return paid - bill
 
 
print(change_due(500, 320))
print(change_due(100, 320))
