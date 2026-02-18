# 🚀 Quick Start Guide

## Fast Setup (2 Minutes)

### Option 1: Run Locally

```bash
# Step 1: Navigate to the project folder
cd "Streamlit Portfolio"

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app.py
```

Your portfolio will open in your browser at `http://localhost:8501`

---

## Customization Checklist

Before sharing your portfolio, update these items in `app.py`:

### 👤 Personal Information (Lines 170-180)
- [ ] Replace `shane.opinion@email.com` with your email
- [ ] Update phone number
- [ ] Add your location

### 🔗 Social Links (Multiple locations)
- [ ] GitHub link
- [ ] LinkedIn URL
- [ ] Personal website (if applicable)

### 💻 Technical Skills
In the **Technical Skills** section, update:
- [ ] Add/remove programming languages
- [ ] Update proficiency levels (0-100)
- [ ] Modify categories as needed

### 🚀 Projects
In the **Projects** section:
- [ ] Replace demo projects with your actual projects
- [ ] Add real GitHub links
- [ ] Update technologies used
- [ ] Add accurate dates

### 📚 Education
- [ ] Update university/institution name
- [ ] Change GPA (if different)
- [ ] Modify relevant coursework
- [ ] Update graduation date

### 🙏 Ministry Information
- [ ] Update organization name (if different from CCF NxtGen)
- [ ] Modify roles and responsibilities
- [ ] Update involvement duration

---

## Feature Highlights

### ✨ What This App Includes

**8 Main Sections:**
1. Home - Introduction & quick stats
2. About Me - Personal story and values
3. Education - Academic background
4. Technical Skills - Interactive skill showcase
5. Projects - Portfolio with filtering
6. Leadership & Ministry - CCF involvement
7. Goals & Vision - Career aspirations
8. Contact - Get in touch

**Interactive Elements:**
- 📊 Charts and data visualizations
- 🎛️ Tab-based navigation
- 📋 Data tables
- 🔍 Project filtering
- 💬 Contact form
- 📈 Progress bars for skills
- ✉️ Email links
- 🌐 External links

---

## Deployment (Bonus Points!)

### Deploy to Streamlit Cloud (Free Hosting)

1. **Create a GitHub Account** (if you don't have one)
   - Go to [github.com](https://github.com)
   - Sign up for free

2. **Upload Your Project to GitHub**
   ```bash
   git init
   git add .
   git commit -m "My portfolio app"
   git remote add origin https://github.com/YOUR-USERNAME/streamlit-portfolio.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Streamlit Cloud**
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "Sign in with GitHub"
   - Click "New app"
   - Select your repository: `streamlit-portfolio`
   - Select branch: `main`
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Your Live Portfolio**
   ```
   https://YOUR-USERNAME-streamlit-portfolio.streamlit.app
   ```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 8501 is already in use"
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: App won't start
**Solution:**
- Check Python version: `python --version` (must be 3.8+)
- Reinstall requirements: `pip install --upgrade -r requirements.txt`
- Clear cache: `streamlit cache clear`

---

## Tips & Tricks

### 🎨 Customize Colors
Edit the CSS in `app.py` (around line 34):
- Change `#0ea5e9` to your preferred color
- Use [coolors.co](https://coolors.co) to find nice color combinations

### 📱 Test on Mobile
Use Streamlit sharing to test on phone:
```bash
streamlit run app.py --logger.level=debug
```

### 🔄 Live Reload
Streamlit automatically reloads when you save the file. Just edit `app.py` and watch it update!

### 📸 Share Your Portfolio
- Share the live link from Streamlit Cloud
- Or run locally and share the code on GitHub
- Add to your resume and LinkedIn profile

---

## Next Steps

1. ✅ Run the app locally
2. ✅ Customize with your information
3. ✅ Test all pages and links
4. ✅ Deploy on Streamlit Cloud (optional)
5. ✅ Share with professors, peers, and recruiters
6. ✅ Keep updating as you learn and grow!

---

## Need Help?

- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Community:** [discuss.streamlit.io](https://discuss.streamlit.io)
- **Python Help:** [python.org](https://www.python.org)

---

## 📚 Resources Included

- `app.py` - Complete application code (1000+ lines)
- `requirements.txt` - All dependencies
- `README.md` - Comprehensive documentation
- `.streamlit/config.toml` - Streamlit configuration
- `QUICKSTART.md` - This file

---

**Happy coding! 🚀**

Good luck with your portfolio and career journey!
