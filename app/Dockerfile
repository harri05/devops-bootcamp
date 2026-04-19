# ================================
# STAGE 1: Builder
# ================================
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build dependencies
COPY requirements.txt .

# Install to a specific directory we'll copy later
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ================================
# STAGE 2: Final Production Image
# ================================
FROM python:3.11-slim AS production

# Create non-root user (security best practice)
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy only the installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY app.py .

# Switch to non-root user
USER appuser

# Environment defaults (overridden at runtime)
ENV APP_ENV=production \
    PORT=5000 \
    REDIS_HOST=redis \
    REDIS_PORT=6379

EXPOSE 5000

# Use exec form (not shell form) — proper signal handling
CMD ["python", "app.py"]
