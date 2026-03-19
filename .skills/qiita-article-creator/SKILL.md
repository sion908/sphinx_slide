---
name: Qiita Article Creator
description: Standardized workflow for creating new Qiita articles with proper naming conventions and file management.
---

# Skill: Qiita Article Creator

## Role
You manage the creation of new Qiita articles following the established workflow and naming conventions.

## Article Creation Workflow

### 1. Naming Convention

New articles should follow this pattern:
```
public/YYYYMMDD_article-title.md
```

Where:
- `YYYYMMDD` = Current date (e.g., 20260316)
- `article-title` = kebab-case version of the article title
- Example: `20260316_flask-sqlspec-crud.md`

### 2. Creation Process

**Step 1: Create new article file**
```bash
npx qiita new YYYYMMDD_article-title
```

**Step 2: Wait for file creation**
- Qiita CLI creates the file with proper frontmatter
- File appears in the current directory
- Initial frontmatter includes placeholder values

**Step 3: Edit the article content**
- Update frontmatter with proper title, tags, etc.
- Write the article content
- Keep the `id` field as null for new articles

**Step 4: Publish the article**
```bash
npx qiita publish YYYYMMDD_article-title
```

### 3. Frontmatter Template

```yaml
---
title: Article Title Here
tags:
  - tag1
  - tag2
  - tag3
private: false
updated_at: 'YYYY-MM-DDTHH:MM:SS+09:00'
id: null
organization_url_name: null
slide: false
ignorePublish: false
---
```

### 4. Important Rules

- **Always use `qiita new` first** - Never create files manually
- **Keep `id: null`** until after first publish
- **Use kebab-case for filenames** - No spaces or special characters
- **Include date prefix** - For proper organization
- **Use public/ directory** - For published articles

### 5. Common Mistakes to Avoid

❌ **Don't**: Create files manually
```bash
# Wrong
touch public/20260316_my-article.md
```

✅ **Do**: Use Qiita CLI
```bash
# Correct
npx qiita new 20260316_my-article
```

❌ **Don't**: Set ID manually
```yaml
# Wrong
id: "some-random-id"
```

✅ **Do**: Let CLI handle it
```yaml
# Correct
id: null
```

❌ **Don't**: Use spaces in filenames
```bash
# Wrong
npx qiita new "20260316 my article"
```

✅ **Do**: Use kebab-case
```bash
# Correct
npx qiita new 20260316_my-article
```

### 6. File Management

After publishing:
- CLI automatically updates the `id` field
- File can be moved to `public/` directory
- Future updates use `qiita publish` command

### 7. Directory Structure

```
qiita/
├── public/                 # Published articles
│   ├── 20260316_flask-sqlspec-crud.md
│   └── 20260315_another-article.md
├── drafts/                 # Draft articles (optional)
└── YYYYMMDD_article-title.md    # New articles before publishing
```

## Usage Examples

### Example 1: Technical Article
```bash
# Create new article about Flask
npx qiita new 20260316_flask-sqlspec-crud

# Edit the file
mv 20260316_flask-sqlspec-crud.md public/
# Update content...

# Publish
npx qiita publish 20260316_flask-sqlspec-crud
```

### Example 2: Tutorial Article
```bash
# Create new tutorial
npx qiita new 20260316_python-beginner-tutorial

# Edit content...
# Publish
npx qiita publish 20260316_python-beginner-tutorial
```

## Output Format

When asked to create a new article, output in this format:

1. **Filename** (following naming convention)
2. **Creation command** to run
3. **Frontmatter template** for the article
4. **Next steps** for writing and publishing

## Quality Checklist

Before publishing:
- [ ] Filename follows YYYYMMDD_kebab-case pattern
- [ ] Created with `qiita new` command
- [ ] Frontmatter is properly formatted
- [ ] Tags are relevant and specific
- [ ] Title is descriptive and engaging
- [ ] Content is well-structured
- [ ] Code blocks are properly formatted
- [ ] Links are working
- [ ] Article passes AI Smell Detector check

## Integration with Other Skills

This skill works with:
- **AI Smell Detector** - For improving article quality
- **Qiita Manager** - For overall repository management

## Troubleshooting

### File Already Exists
```bash
Error: 'filename.md' is already exist
```
**Solution**: Choose a different filename or delete the existing file

### ID Required Error
```bash
filename: idは文字列で入力してください
```
**Solution**: Ensure the file was created with `qiita new` and has `id: null`

### Not Found Error
```bash
QiitaNotFoundError: {"message":"Not found"}
```
**Solution**: Article doesn't exist on Qiita yet, use `qiita publish` first
