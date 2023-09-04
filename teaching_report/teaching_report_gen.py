import os
from datetime import datetime
import re
base_dir = "teaching_report"
html_filename = "teaching_report.html"

# Initialize an empty list to store valid subdirectory details.
subdirectories_info = []


MONTHS = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    """Parse date string using regex and manual month conversion."""
    match = re.match(r'(\d{1,2})([A-Za-z]+)(\d{4})', date_str)
    
    if not match:
        raise ValueError(f"Unable to parse date from {date_str}")

    day, month, year = match.groups()

    if month not in MONTHS:
        raise ValueError(f"Invalid month {month} in date {date_str}")

    return datetime(int(year), MONTHS[month], int(day))


# Traverse the base directory
for subdir in os.listdir(base_dir):
    full_path = os.path.join(base_dir, subdir)
    
    if not os.path.isdir(full_path):  # Skip if it's not a directory
        continue

    # Check for valid subdirectory format
    if "_" in subdir:
        # Extract the date and subject
        date_part, subject_part = subdir.split("_", 1)
        
        # try:
            # Parse date part to a date object
        date_object = parse_date(date_part)
        # except ValueError:
        #     # Skip if the date format is not correct
        #     continue

        # Assuming there's only one PDF per subdirectory, find the PDF file.
        pdf_files = [f for f in os.listdir(full_path) if f.endswith(".pdf")]

        if pdf_files:
            pdf_file = pdf_files[0]
            pdf_path = os.path.join(full_path, pdf_file)
            subdirectories_info.append((date_object, date_part, subject_part, pdf_path))


# Sort the subdirectories_info based on date for proper ordering in the HTML
subdirectories_info.sort(key=lambda x: x[0])

# Generate HTML content
html_content = """<!DOCTYPE HTML>
<!--
	Editorial by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Teaching Report</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Main -->
					<div id="main">
						<div class="inner">

							<!-- Header -->
								<header id="header">
									<a href="index.html" class="logo"><strong>Teaching Report </strong> </a>
			
								</header>

							<!-- Content -->
								<section>
									<header class="main">
										<h1>Teaching Report</h1>
									</header>

									

									<h3>Collected Teaching Report From Past Days </h3>
"""

for _, date_part, subject_part, pdf_path in subdirectories_info:
    html_content += f'<li><a href="{pdf_path}">{date_part} - {subject_part}</a></li>\n'

html_content += """
</section>

						</div>
					</div>

				<!-- Sidebar -->
					<div id="sidebar">
						<div class="inner">

							<!-- Search -->
								<section id="search" class="alt">
									<form method="post" action="#">
										<input type="text" name="query" id="query" placeholder="Search" />
									</form>
								</section>

							<!-- Menu -->
								<nav id="menu">
									<header class="major">
										<h2>Menu</h2>
									</header>
									<ul>
										<li><a href="index.html">Homepage</a></li>
										<li>
											<span class="opener">IGCSE Mathematics (0580)</span>
											<ul>
												<li><a href="math_0580_project.html">project</a></li>
												<li><a href="math_0580_content.html">content</a></li>
												<li><a href="#">exam</a></li>
												
											</ul>
										</li>
										<li>
											<span class="opener">Ningboness Bible</span>
											<ul>
												<li><a href="MÔ-T'A.html">MÔ-T'A DJÜN FOH-ING SHÜ 马太福音</a></li>
												
												<li><a href="#"></a></li>
											</ul>
										</li>
										<li><a href="teaching_report.html">Teaching Report</a></li>
										
							<section>
								<header class="major">
									<h2>Get in touch</h2>
								</header>
								<p>Feel free to approach me as followed:</p>
								<ul class="contact">
									<li class="icon solid fa-envelope"><a>wangxiiq200@icloud.com</a></li>
									<li class="icon solid fa-envelope"><a>120040088@link.cuhk.edu.cn</a></li>
									<li class="icon solid fa-phone">(+1) 928 225 8995</li>
									<li class="icon solid fa-home">1475 Tadmor Street <br />
									Merrick, NY 11566</li>
								</ul>
							</section>

							<!-- Footer -->
								<footer id="footer">
									<p class="copyright">&copy; All rights reserved.</p>
								</footer>

						</div>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
"""

# Save to teaching_report.html
with open(html_filename, 'w') as html_file:
    html_file.write(html_content)

print(f"Generated {html_filename} with links to PDF files.")
