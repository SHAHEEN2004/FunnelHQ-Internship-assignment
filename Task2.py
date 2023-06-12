def get_user_input():
    company_name = input("Enter the company name: ")
    city = input("Enter the city: ")
    date = input("Enter the date: ")
    spokesperson_name = input("Enter the spokesperson's name: ")
    title = input("Enter the spokesperson's title: ")
    website_url = input("Enter the website URL: ")

    return company_name, city, date, spokesperson_name, title, website_url

def generate_press_release(company_name, city, date, spokesperson_name, title, website_url):
    press_release = f"{company_name} Revolutionizes the Industry with the Launch of AI Democratizing SaaS Tool\n\n"
    press_release += f"{city}, {date} - {company_name}, a leading innovator in the AI industry, is proud to announce the launch of its groundbreaking AI democratizing Software-as-a-Service (SaaS) tool. This cutting-edge solution is set to revolutionize the way businesses leverage artificial intelligence, making it accessible to all, regardless of technical expertise.\n\n"
    press_release += "Key Features and Benefits:\n"
    press_release += "- Democratizing AI: [Company Name]'s SaaS tool breaks down the barriers to AI adoption by offering a user-friendly interface and pre-built AI models, eliminating the need for coding or data science skills.\n"
    press_release += "- Streamlined Workflow: The tool simplifies the AI development process, enabling businesses to easily train, deploy, and manage AI models within a single platform.\n"
    press_release += "- Scalability and Flexibility: With [Company Name]'s SaaS tool, businesses can effortlessly scale AI applications to meet their evolving needs, driving innovation and efficiency across various industries.\n"
    press_release += "- Powerful Insights: Leveraging advanced machine learning algorithms, the tool delivers actionable insights and predictive analytics, empowering businesses to make data-driven decisions and gain a competitive edge.\n\n"
    press_release += f'"We are thrilled to introduce our AI democratizing SaaS tool to the market," said {spokesperson_name}, {title} at {company_name}. "By making AI accessible to a wider audience, we are enabling businesses of all sizes to harness the transformative power of artificial intelligence, driving growth and innovation."\n\n'
    press_release += f"{company_name}'s AI democratizing SaaS tool is available for a free trial, allowing businesses to experience the benefits firsthand. To learn more, visit {website_url}.\n\n"
    press_release += f"About {company_name}:\n"
    press_release += f"{company_name} is a leading provider of AI solutions, dedicated to democratizing access to artificial intelligence. With a mission to empower businesses with the tools they need to thrive in the digital age, {company_name} is revolutionizing industries and driving innovation through cutting-edge AI technologies."

    return press_release

# Example usage:
company_name, city, date, spokesperson_name, title, website_url = get_user_input()
press_release = generate_press_release(company_name, city, date, spokesperson_name, title, website_url)
print(press_release)