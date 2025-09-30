# Contributing to AI Content Platform

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/ai-content-platform.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit with clear messages
7. Push to your fork
8. Create a Pull Request

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install pytest pytest-asyncio black flake8 mypy

# Setup pre-commit hooks
pre-commit install
```

## Code Style

We follow PEP 8 with some modifications:

- Line length: 100 characters
- Use Black for formatting
- Use isort for import sorting
- Type hints required for public functions

### Format Code

```bash
# Format with Black
black app/

# Sort imports
isort app/

# Check with flake8
flake8 app/

# Type check with mypy
mypy app/
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_main.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Write tests for new features
- Maintain or improve code coverage
- Use pytest fixtures
- Follow async/await patterns

Example test:
```python
@pytest.mark.asyncio
async def test_create_content(client, auth_headers):
    response = await client.post(
        "/api/v1/content/",
        json={"title": "Test", "content_type": "text"},
        headers=auth_headers
    )
    assert response.status_code == 201
```

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing performed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code formatted
```

## Commit Messages

Follow conventional commits:

```
type(scope): subject

body (optional)

footer (optional)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat(api): add content versioning endpoint
fix(auth): resolve token expiration issue
docs(readme): update installation instructions
```

## Project Structure

```
ai-content-platform/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Core functionality
│   ├── models/       # Database models
│   ├── schemas/      # Pydantic schemas
│   ├── services/     # Business logic
│   ├── agents/       # LangChain agents
│   └── main.py       # Application entry
├── tests/            # Test files
├── docs/             # Documentation
└── docker/           # Docker configs
```

## Adding New Features

### New API Endpoint

1. Create schema in `app/schemas/`
2. Create model in `app/models/` (if needed)
3. Create endpoint in `app/api/endpoints/`
4. Add tests in `tests/`
5. Update documentation

### New AI Agent

1. Create agent class extending `BaseAgent`
2. Implement required methods
3. Add to agent registry
4. Write tests
5. Document usage

## Documentation

- Update README.md for user-facing changes
- Update API.md for API changes
- Update ARCHITECTURE.md for structural changes
- Add docstrings to new functions
- Include examples in docstrings

## Review Process

1. Automated checks run on PR
2. Maintainer reviews code
3. Feedback addressed
4. Approved and merged

## Release Process

We follow semantic versioning (MAJOR.MINOR.PATCH):

- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

## Questions?

- Open an issue for bugs
- Use discussions for questions
- Email: dev@example.com

Thank you for contributing!
