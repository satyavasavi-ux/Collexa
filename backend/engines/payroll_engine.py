from decimal import Decimal
from typing import Dict, Any

class PayrollCalculator:
    @staticmethod
    def generate_salary_slip(employee_id: str, employee_name: str, designation: str, basic_pay: Decimal, days_present: int, total_working_days: int = 30) -> Dict[str, Any]:
        # Allowance rates
        hra_rate = Decimal("0.24") # 24% HRA
        da_rate = Decimal("0.38")  # 38% Dearness Allowance
        ta = Decimal("3600.00")    # Fixed Travel Allowance
        special_allowance = Decimal("5000.00")

        # Pro-rata basic based on attendance
        earned_basic = (basic_pay / Decimal(str(total_working_days))) * Decimal(str(days_present))
        hra = earned_basic * hra_rate
        da = earned_basic * da_rate
        gross_salary = earned_basic + hra + da + ta + special_allowance

        # Deductions
        pf = min(Decimal("1800.00"), earned_basic * Decimal("0.12"))
        prof_tax = Decimal("200.00")
        income_tax = gross_salary * Decimal("0.10") if gross_salary > Decimal("50000.00") else Decimal("0.00")
        total_deductions = pf + prof_tax + income_tax
        net_salary = gross_salary - total_deductions

        return {
            "employee_id": employee_id,
            "employee_name": employee_name,
            "designation": designation,
            "days_worked": f"{days_present}/{total_working_days}",
            "earnings": {
                "basic_pay": round(earned_basic, 2),
                "house_rent_allowance": round(hra, 2),
                "dearness_allowance": round(da, 2),
                "travel_allowance": round(ta, 2),
                "special_allowance": round(special_allowance, 2),
                "gross_salary": round(gross_salary, 2)
            },
            "deductions": {
                "provident_fund": round(pf, 2),
                "professional_tax": round(prof_tax, 2),
                "tax_deducted_at_source": round(income_tax, 2),
                "total_deductions": round(total_deductions, 2)
            },
            "net_salary_payable": round(net_salary, 2)
        }
