# Shane Adrian C. Opinion - Personal Portfolio & Autobiography

A comprehensive, interactive Streamlit application showcasing my journey as a BSIT student, aspiring software developer, and Christian youth leader.

## 📖 About This Portfolio

This portfolio combines my professional aspirations in software development with my passion for Christian youth ministry. It tells my story through an interactive web application built entirely with Streamlit.

### 🎯 Key Focus Areas
- **Software Development Skills**: Java, Spring Boot, React, and emerging technologies
- **Academic Journey**: BSIT program highlights and learning outcomes
- **Projects Portfolio**: Academic projects, React games, Spring Boot applications, and capstone ideas
- **Christian Youth Ministry**: Leadership through CCF NxtGen
- **Career Vision**: Goals and aspirations for meaningful impact

---

## 🚀 Features

### 📱 User Interface
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Professional Styling**: Custom CSS with gradient colors and modern aesthetics
- **Intuitive Navigation**: Sidebar-based navigation with 8 distinct sections
- **Dark Mode Ready**: Compatible with Streamlit light/dark themes

### 📑 Sections Included

1. **🏠 Home** - Welcome with quick stats and key highlights
2. **👋 About Me** - Personal story, values, and interests
3. **📚 Education** - BSIT program details and achievements
4. **💻 Technical Skills** - Interactive skill breakdown with proficiency levels
5. **🚀 Projects** - Portfolio with project filtering and details
6. **🙏 Leadership & Ministry** - CCF NxtGen involvement and activities
7. **🎯 Goals & Vision** - Career path and life aspirations
8. **📬 Contact** - Contact form, links, and ways to connect

### 🎨 Interactive Components

**Streamlit Components Used:**
- `st.title()`, `st.header()`, `st.subheader()` - Text elements
- `st.columns()` and `st.container()` - Layout management
- `st.tabs()` and `st.expander()` - Navigation elements
- `st.metric()` - Key statistics display
- `st.progress()` - Skill proficiency visualization
- `st.form()` and `st.text_input()` - Contact form
- `st.selectbox()` - Project filtering
- `st.dataframe()` - Table display
- `st.link_button()` - External links
- `st.markdown()` - Custom HTML/CSS styling
- Plotly charts - Interactive visualizations (pie, line graphs)

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download
```bash
# Navigate to project directory
cd "Streamlit Portfolio"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 🎨 Customization Guide

### Update Personal Information

Replace these placeholders in `app.py`:
- `shane.opinion@email.com` → Your email
- `+63 (XXX) XXX-XXXX` → Your phone number
- GitHub, LinkedIn, and social media links
- Contact form email destination

### Modify Technical Skills

Edit the `skills_data` dictionary in the Technical Skills section:
```python
skills_data = {
    "Skill": ["Your Skill 1", "Your Skill 2"],
    "Category": ["Backend", "Frontend"],
    "Proficiency": [90, 85]
}
```

### Update Projects

Modify the `projects` list in the Projects section:
```python
projects = [
    {
        "title": "Your Project Title",
        "category": "Full-Stack",
        "description": "Your description",
        "technologies": ["Tech1", "Tech2"],
        "link": "https://github.com/yourlink",
        "date": "2024"
    }
]
```

### Customize Colors & Styling

Edit the CSS in the `<style>` section:
- Primary color: `#0ea5e9` (blue)
- Accent colors: `#3b82f6`, `#10b981`, `#f59e0b`, `#a855f7`
- Background: `#f0f9ff`, `#faf5ff`, `#f0fdf4`

---

## 🌐 Deployment on Streamlit Community Cloud

### Benefits of Cloud Deployment
✅ Free hosting  
✅ Automatic updates from GitHub  
✅ Real-time collaboration  
✅ Easy sharing with link  

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Portfolio app"
   git remote add origin https://github.com/yourusername/streamlit-portfolio.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with GitHub account
   - Click "New app"
   - Select your repository
   - Select branch: `main`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Share Your Portfolio**
   - Your app will be available at:
   ```
   https://[username]-streamlit-portfolio.streamlit.app
   ```

### Environment Variables (if needed)
Create a `.streamlit/secrets.toml` file:
```toml
email_password = "your_email_password"
github_token = "your_github_token"
```

---

## 📁 Project Structure

```
Streamlit Portfolio/
├── app.py                          # Main application (1000+ lines)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── .streamlit/
    └── config.toml                 # Streamlit configuration
```

---

## 📚 Technologies Used

### Core Dependencies
- **Streamlit** v1.28.1 - Web application framework
- **Pandas** v2.1.3 - Data manipulation and analysis
- **NumPy** v1.24.3 - Numerical computing
- **Plotly** v5.17.0 - Interactive data visualizations

### Browser Compatibility
- Chrome/Chromium ✅
- Firefox ✅
- Safari ✅
- Edge ✅

---

## 🎓 Learning Resources

This project demonstrates:
- ✅ Responsive web design
- ✅ Component-based architecture
- ✅ Data visualization
- ✅ Form handling
- ✅ Custom CSS styling in Python
- ✅ Multi-page navigation
- ✅ Interactive UI elements

---

## 💡 Enhancement Ideas

Future improvements you could add:
- [ ] Dark mode toggle
- [ ] Blog/Articles section
- [ ] Project showcase gallery with images
- [ ] Testimonials from professors/colleagues
- [ ] Skills assessment quiz
- [ ] Certificate showcase
- [ ] GitHub integration to fetch real projects
- [ ] Analytics dashboard
- [ ] Newsletter signup
- [ ] Social media integration
- [ ] Animation effects
- [ ] Multi-language support

---

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio!

### Tips for Customization:
1. Keep your information accurate and up-to-date
2. Add real links to your projects and profiles
3. Update achievements as you accomplish goals
4. Maintain professional tone throughout
5. Test on multiple devices before sharing
6. Get feedback from friends and mentors

---

## 📝 Notes

- The contact form is a demo - consider integrating with Formspree, EmailJS, or similar service for real functionality
- Update all external links to your actual profiles
- Replace placeholder metrics with your real statistics
- Add projects as you complete them
- Keep content fresh and relevant

---

## 📄 License

This project is open source. Feel free to use it as a template for your own portfolio.

---

## 🙏 Acknowledgments

- Built with Streamlit, an amazing framework for data apps
- Inspired by modern portfolio best practices
- Created with passion and purpose

---

**Made with ❤️ by Shane Adrian C. Opinion**  
*BSIT Student | Aspiring Software Developer | Christian Youth Leader*  
*February 2026*
