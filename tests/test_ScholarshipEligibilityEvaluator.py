import pytest

from src.ScholarshipEligibilityEvaluator import *

CTES = {
    'ACCEPTED':   "Applicant meets all scholarship requirements.",
    'REJECT_AGE': "Applicant is younger than the minimum age.",
    'REVIEW_AGE': "Applicant is under 18 and requires manual review.",
    'REJECT_GPA': "GPA is below the minimum required.",
    'REVIEW_GPA': "GPA is in the manual review range.",
    'REJECT_FREQUENCY': "Attendance rate is below the minimum required.",
    'REVIEW_FREQUENCY': "Attendance rate is in the manual review range.",
    'REJECT_COURSES': "Required courses have not been completed.",
    'REJECT_DISCIPLINARY': "Applicant has a disciplinary record."
}

##### APPROVED TEST #####

def test_scholarship_eligibility_approved():
    #Arrange
    age, gpa, frequency = 19, 8, 81
    has_courses, record = True, False

    #Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

    #Assert
    expected_result = EvaluationResult(Status.APPROVED, 
                                       [CTES['ACCEPTED']])
    assert result == expected_result

##### AGE TESTS #####

@pytest.mark.parametrize("age, gpa, frequency, has_courses, record, expected_status, expected_reason", [
    (15, 8, 80, True, False, Status.REJECTED, CTES['REJECT_AGE']),
    (16, 8, 80, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_AGE']),
    (17, 8, 80, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_AGE']),
    (18, 8, 80, True, False, Status.APPROVED, CTES['ACCEPTED']),])

def test_age_limits(age, gpa, frequency, has_courses, record, expected_status, expected_reason):
    # Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    
    # Assert
    expected_result = EvaluationResult(expected_status, [expected_reason])
    assert result == expected_result

##### GPA LIMITS TESTS #####

@pytest.mark.parametrize("age, gpa, frequency, has_courses, record, expected_status, expected_reason", [
    (18, 5.5, 80, True, False, Status.REJECTED, CTES['REJECT_GPA']),
    (18, 6, 80, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_GPA']),
    (18, 6.5, 80, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_GPA']),
    (18, 7, 80, True, False, Status.APPROVED, CTES['ACCEPTED']),
    (18, 7.5, 80, True, False, Status.APPROVED, CTES['ACCEPTED'])])

def test_gpa_limits(age, gpa, frequency, has_courses, record, expected_status, expected_reason):
    # Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    
    # Assert
    expected_result = EvaluationResult(expected_status, [expected_reason])
    assert result == expected_result


##### FREQUENCY TESTS #####

@pytest.mark.parametrize("age, gpa, frequency, has_courses, record, expected_status, expected_reason", [
    (18, 8, 74, True, False, Status.REJECTED, CTES['REJECT_FREQUENCY']),
    (18, 8, 75, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_FREQUENCY']),
    (18, 8, 77, True, False, Status.MANUAL_REVIEW, CTES['REVIEW_FREQUENCY']),
    (18, 8, 80, True, False, Status.APPROVED, CTES['ACCEPTED']),
    (18, 8, 81, True, False, Status.APPROVED, CTES['ACCEPTED']),
])

def test_frequency_limits(age, gpa, frequency, has_courses, record, expected_status, expected_reason):
    # Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    
    # Assert
    expected_result = EvaluationResult(expected_status, [expected_reason])
    assert result == expected_result

##### TEST BOOLEAN VALUES TESTS #####
@pytest.mark.parametrize("age, gpa, frequency, has_courses, record, expected_status, expected_reason", [
    (18, 8, 80, False, False, Status.REJECTED, CTES['REJECT_COURSES']),
    (18, 8, 80, True, True, Status.REJECTED, CTES['REJECT_DISCIPLINARY'])]
    )

def test_boolean_reject_limits(age, gpa, frequency, has_courses, record, expected_status, expected_reason):
    # Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    
    # Assert
    expected_result = EvaluationResult(expected_status, [expected_reason])
    assert result == expected_result


##### INVALID GPA TESTS #####

def test_gpa_below_0_raise_error():
    #Arrange
    age, gpa, frequency = 19, -1, 81
    has_courses, record = True, False

    #Act and Assert
    with pytest.raises(ValueError):
        result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    

def test_gpa_greater_than_10_raise_error():
    #Arrange
    age, gpa, frequency = 19, 11, 81
    has_courses, record = True, False

    #Act and Assert
    with pytest.raises(ValueError):
        result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

##### INVALID FREQUENCY VALUES ####

def test_frequency_below_0_raise_error():
    #Arrange
    age, gpa, frequency = 19, 8, -1.0
    has_courses, record = True, False

    #Act and Assert
    with pytest.raises(ValueError):
        result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

def test_frequency_greater_than_100_raise_error():
        #Arrange
    age, gpa, frequency = 19, 45, 101.0
    has_courses, record = True, False

    #Act and Assert
    with pytest.raises(ValueError):
        result = evaluate_scholarship(age, gpa, frequency, has_courses, record)

##### MULTIPLE REASONS ####

### DEFINE CTES
ALL_REJECTIONS = [
    CTES['REJECT_AGE'], CTES['REJECT_GPA'], CTES['REJECT_FREQUENCY'],
    CTES['REJECT_COURSES'], CTES['REJECT_DISCIPLINARY']
]

GPA_AND_FREQ_REJECTIONS = [
    CTES['REJECT_GPA'], CTES['REJECT_FREQUENCY']
]

COURSES_AND_DISC_REJECTIONS = [
    CTES['REJECT_COURSES'], CTES['REJECT_DISCIPLINARY']
]

GPA_REJECTION_ONLY = [
    CTES['REJECT_GPA']
]

ALL_REVIEWS = [
    CTES['REVIEW_AGE'], CTES['REVIEW_GPA'], CTES['REVIEW_FREQUENCY']
]

@pytest.mark.parametrize("age, gpa, frequency, has_courses, record, expected_status, expected_reason", [
    (15, 4, 70, False, True, Status.REJECTED, ALL_REJECTIONS),
    (18, 5, 70, True, False, Status.REJECTED, GPA_AND_FREQ_REJECTIONS),
    (18, 8, 80, False, True, Status.REJECTED, COURSES_AND_DISC_REJECTIONS),
    #This case has a "review reason" and a "reject reason", but it should be rejected
    (17, 4, 80, True, False, Status.REJECTED, [CTES['REJECT_GPA']]),
    (17, 6.5, 76, True, False, Status.MANUAL_REVIEW, ALL_REVIEWS)
    ]
                        
    )
def test_multiple_reasons_to_reject_or_review(age, gpa, frequency, has_courses, record, expected_status, expected_reason):
    # Act
    result = evaluate_scholarship(age, gpa, frequency, has_courses, record)
    
    # Assert
    expected_result = EvaluationResult(expected_status, expected_reason)
    assert result == expected_result

#def test_