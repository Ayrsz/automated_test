import pytest

from src.ScholarshipEligibilityEvaluator import *

def test_eligibility_approved_case():
    #Arrange
    age, gpa, frequency = 19, 8, 81
    has_courses, record = True, False

    #Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

    #Assert
    expected_result = EvaluationResult(Status.APPROVED, 
                                       ["Applicant meets all scholarship requirements."])
    assert result == expected_result

def test_age_below_16_case():
    #Arrange
    age, gpa, frequency = 15, 8, 81
    has_courses, record = True, False

    #Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

    #Assert
    expected_result = EvaluationResult(Status.REJECTED, 
                                       ["Applicant is younger than the minimum age."])
    
    assert result == expected_result

def test_age_16_case():
    pass
