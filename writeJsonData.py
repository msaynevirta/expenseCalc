import json

def writeYear(yearDict, year):
    return yearDict

def writeMonth(monthDict, monthStr):
    return monthDict

def writeEntry(entryDict, dateStr, amount, taxes, beneficiary, subCat, mainCat, paymentMethod):
    return entryDict

def main():
    baseDict = {
        "expenses": {}
    }
        
    yearDict = {
            "year": int(year),
            "months": {}
    }
                
    monthDict = {
        "month": str(monthStr),
        "entries": []
    }
            
    entryDict = {
        "date": str(dateStr),
        "amount": float(amount),
        "taxes": [], # [[amount, tax rate], [amount, tax rate]]
        "beneficiary": str(beneficiary),
        "subcategory": str(subCat),
        "category": str(mainCat),
        "paymentMethod": [] # [payment type, card type, bank]
    }
