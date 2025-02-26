import math
from collections import Counter


def calculate_entropy(text):
    """Calculate the entropy of a given text."""
    if not text:
        return 0

    # Count the frequency of each character
    freq = Counter(text)
    total_chars = len(text)

    # Compute entropy
    entropy = -sum((count / total_chars) * math.log2(count / total_chars)
                   for count in freq.values())

    return entropy


# Example usage
paragraph_c = """谨此提交联合检查组 2024 年年度报告,其中介绍了联检组 2024 年 1 月 1 日
至 12 月 31 日期间的活动,并概述了 2025 年工作方案。
联检组 2024 年工作计划包括从 2023 年结转的 3 项审查和 2024 年工作方案
中的 6 项审查。此外,在 2024 年下半年开始时,联检组在现行工作方案中增加
了对联合国系统各组织监察员和调解职能的审查。
关于联检组的产出,2024 年发布了六个产品:三份关于全系统审查的报
告、一份关于单个组织的管理和行政审查的报告以及两份说明。
2022 年开展的自我评估活动所产生建议的落实是联检组 2024 年的高度优先
事项之一。就 26 项建议采取了行动,执行率达到 54%。其余 22项建议正在落实
中。联检组的目标是到 2025 年底全面落实其余建议。
2024 年,联检组按照大会要求着力编写 2020-2029 年战略框架中期评估报
告。这一评估情况可在联检组网站上查阅,其中包括经修订的成果框架和对应
于业绩指标的联检组成绩评价。
展望 2025 年,联检组在工作方案中列入了六项全系统审查和一项对单一组
织的管理和行政审查。年度工作计划将包括 2025 年工作方案审查和 2024 年开始
的五项审查,这些审查定于 2025 年第三季度完成。必须指出的是,所有审查都
遵守根据所审查主题的范围和复杂性估计的既定时限。通常而言,完成一份报
告(即编写报告以供正式编辑)的平均时间就单一组织的审查而言为 12 个月,就
涵盖 28 个参加组织的全系统审查为 18 至 24 个月。
最后,我谨代表联检组各个检查专员感谢联检组秘书处工作人员的执着努
力和宝贵贡献,感谢每个参加组织的协调人给予我们的支持及合作。"""


paragraph_E = """
I have the honour to present the annual report of the Joint Inspection Unit for
the year 2024, which contains an account of the Unit’s activities for the period from
1 January to 31 December 2024 and a summary of its programme of work for 2025.
The Unit’s workplan for 2024 comprised three reviews carried over from 2023
and six reviews in its programme of work for 2024. Furthermore, at the start of the
second half of 2024, the Unit added a review of the ombudsman and mediation
function in United Nations system organizations to its ongoing programme of work.
Regarding the Unit’s outputs, six products were released in 2024: three reports
on system-wide reviews, one report on the management and administration review of
a single organization, and two notes.
The implementation of the recommendations from the self-assessment exercise
conducted in 2022 was among the high priorities for the Unit in 2024. Action was
taken on 26 recommendations, achieving a 54 per cent implementation rate. The
remaining 22 recommendations are in progress. The Unit will aim to fully implement
the remaining recommendations by the end of 2025.
In 2024, the Unit worked on preparing its report on the midpoint assessment of
the 2020–2029 strategic framework, as requested by the General Assembly. This
assessment is available on the JIU website and comprises a revised results framework
and an appraisal of the Unit’s achievements against performance indicators.
Looking ahead to 2025, the Unit included six system-wide reviews and one
management and administration review of a single organization in its programme of
work. The workplan for the year will comprise the 2025 programme of work reviews
and the five reviews that were begun in 2024, which are scheduled to be completed
in the third quarter of 2025. It is important to point out that all the reviews adhere to
established time frames that are estimated on the basis of the scope and complexity
of the subject under review. Typically, the average time to complete a report
(i.e. prepare it for submission for official editing) is 12 months for single-organization
reviews and 18 to 24 months for system-wide reviews, which cover 28 participating
organizations.
In closing, I would like to acknowledge, on behalf of the JIU inspectors, the
commitment and valuable contribution of the Unit’s secretariat staff and the support
and cooperation that we receive from the focal points in each of the participating
organizations.

"""

paragraph_E_t = """
I hereby submit the Joint Inspection Unit (JIU) Annual Report for 2024, which outlines the activities of the JIU from January 1 to December 31, 2024, and provides an overview of the 2025 work program.

The JIU’s 2024 work plan included three reviews carried over from 2023 and six reviews from the 2024 work program. Additionally, at the beginning of the second half of 2024, the JIU added a review of the ombudsman and mediation functions of organizations within the United Nations system to its current work program.

Regarding the JIU’s outputs, six products were released in 2024: three reports on system-wide reviews, one report on the management and administration review of a single organization, and two notes.

The implementation of recommendations from the self-evaluation conducted in 2022 was one of the JIU’s top priorities in 2024. Actions were taken on 26 recommendations, achieving an implementation rate of 54%. The remaining 22 recommendations are in the process of being implemented. The JIU aims to fully implement the remaining recommendations by the end of 2025.

In 2024, as requested by the General Assembly, the JIU focused on preparing the mid-term evaluation report of the 2020–2029 Strategic Framework. The evaluation results are available on the JIU website, including the revised results framework and the JIU’s performance assessment corresponding to performance indicators.

Looking ahead to 2025, the JIU has included six system-wide reviews and one management and administration review of a single organization in its work program. The annual work plan will include reviews from the 2025 work program as well as five reviews that began in 2024, scheduled for completion in the third quarter of 2025. It is important to note that all reviews adhere to the established timeframes estimated based on the scope and complexity of the subject under review. Generally, the average time required to complete a report (from drafting to formal editing) is 12 months for a single organization review and 18 to 24 months for a system-wide review covering 28 participating organizations.

Finally, on behalf of all JIU Inspectors, I extend my gratitude to the staff of the JIU Secretariat for their dedication and valuable contributions, as well as to the coordinators of each participating organization for their support and cooperation.

"""


entropy_value_c = calculate_entropy(paragraph_c)
entropy_value_E = calculate_entropy(paragraph_E)
entropy_value_E_t = calculate_entropy(paragraph_E_t)

print(f"Entropy of the paragraph Chinese : {entropy_value_c:.4f}")
print(f"Entropy of the paragraph English orignial: {entropy_value_E:.4f}")
print(f"Entropy of the paragraph English translated: {entropy_value_E_t:.4f}")
