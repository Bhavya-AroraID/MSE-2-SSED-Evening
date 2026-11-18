import sys

def create_pdf(filename):
    pages_text = [
        # Page 1
        [
            ("BT /F2 18 Tf 50 780 Td (KIET Group of Institutions) Tj ET", 0),
            ("BT /F1 11 Tf 50 762 Td (Department of Computer Science & Engineering - AIML) Tj ET", 0),
            ("BT /F1 11 Tf 50 748 Td (Software Engineering and DevOps (AI310B) - MSE 2 (Set 2 - Evening Shift)) Tj ET", 0),
            ("BT /F2 13 Tf 50 715 Td (A. Student Information) Tj ET", 0),
            ("BT /F1 10 Tf 60 695 Td (Student Name:         Bhavya Arora) Tj ET", 0),
            ("BT /F1 10 Tf 60 680 Td (Roll Number:          [ENTER_YOUR_COLLEGE_ROLL_NUMBER]) Tj ET", 0),
            ("BT /F1 10 Tf 60 665 Td (Section:              [ENTER_YOUR_SECTION]) Tj ET", 0),
            ("BT /F1 10 Tf 60 650 Td (Branch / Course:      BTech CSE AI&ML) Tj ET", 0),
            ("BT /F1 10 Tf 60 635 Td (College:              KIET Group of Institutions) Tj ET", 0),
            ("BT /F1 10 Tf 60 620 Td (GitHub Username:      Bhavya-AroraID) Tj ET", 0),
            ("BT /F1 10 Tf 60 605 Td (Docker Hub Username:  bhavya2718) Tj ET", 0),
            ("BT /F2 13 Tf 50 575 Td (B. Repository & Submission URLs) Tj ET", 0),
            ("BT /F1 10 Tf 60 555 Td (GitHub Fork:          https://github.com/Bhavya-AroraID/MSE-2-SSED-Evening) Tj ET", 0),
            ("BT /F1 10 Tf 60 540 Td (Target Examination:   https://github.com/atindeRR/MSE-2-SSED-Evening) Tj ET", 0),
            ("BT /F1 10 Tf 60 525 Td (Pull Request URL:     https://github.com/atindeRR/MSE-2-SSED-Evening/pull/[PR_NUMBER]) Tj ET", 0),
            ("BT /F1 10 Tf 60 510 Td (Docker Hub Frontend:  https://hub.docker.com/r/bhavya2718/frontend) Tj ET", 0),
            ("BT /F1 10 Tf 60 495 Td (Docker Hub Backend:   https://hub.docker.com/r/bhavya2718/backend) Tj ET", 0),
            ("BT /F1 10 Tf 60 480 Td (Actions Workflow:     https://github.com/Bhavya-AroraID/MSE-2-SSED-Evening/actions) Tj ET", 0),
            ("BT /F2 13 Tf 50 450 Td (C. Architecture & Deliverables Summary) Tj ET", 0),
            ("BT /F1 10 Tf 60 432 Td (1. Frontend: Multi-stage build (node:20-slim build, nginx:1.27-alpine runtime).) Tj ET", 0),
            ("BT /F1 10 Tf 60 417 Td (   Reverse-proxies /api/ and /health to http://backend:3000. Port 80 exposed.) Tj ET", 0),
            ("BT /F1 10 Tf 60 402 Td (2. Backend: Production multi-stage build (node:20-alpine, USER node, port 3000).) Tj ET", 0),
            ("BT /F1 10 Tf 60 387 Td (3. Compose: 4 services (frontend, backend, postgres, redis) on taskflow bridge.) Tj ET", 0),
            ("BT /F1 10 Tf 60 372 Td (   Named volume postgres_data, isolated db ports, and service_healthy checks.) Tj ET", 0),
            ("BT /F1 10 Tf 60 357 Td (4. Deploy Compose: Published Docker Hub images (bhavya2718/backend:latest).) Tj ET", 0),
            ("BT /F1 10 Tf 60 342 Td (5. CI/CD Pipeline: Automated build, 4 tags push, deploy, and 12 Jest API tests.) Tj ET", 0),
            ("BT /F2 10 Tf 50 50 Td (Page 1 of 2 - Software Engineering & DevOps (AI310B)) Tj ET", 0)
        ],
        # Page 2
        [
            ("BT /F2 13 Tf 50 780 Td (D. Implementation Evidence & Test Verification) Tj ET", 0),
            ("BT /F2 10 Tf 60 755 Td (1. Frontend & Backend Docker Image Build) Tj ET", 0),
            ("BT /F1 9 Tf 70 740 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: Docker build successful - vite build in 596ms]) Tj ET", 0),
            ("BT /F2 10 Tf 60 715 Td (2. Docker Compose Running Services (docker compose ps)) Tj ET", 0),
            ("BT /F1 9 Tf 70 700 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: 4 containers Up (healthy) on taskflow network]) Tj ET", 0),
            ("BT /F2 10 Tf 60 675 Td (3. Health Check & API Verification) Tj ET", 0),
            ("BT /F1 9 Tf 70 660 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: GET /health -> status: ok, postgres: ok, redis: ok]) Tj ET", 0),
            ("BT /F2 10 Tf 60 635 Td (4. Docker Hub Image Tags (v1 and latest)) Tj ET", 0),
            ("BT /F1 9 Tf 70 620 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: bhavya2718/frontend and bhavya2718/backend tags]) Tj ET", 0),
            ("BT /F2 10 Tf 60 595 Td (5. GitHub Actions CI/CD Pipeline Execution) Tj ET", 0),
            ("BT /F1 9 Tf 70 580 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: .github/workflows/cd.yml execution green]) Tj ET", 0),
            ("BT /F2 10 Tf 60 555 Td (6. Instructor Pull Request CI Checks) Tj ET", 0),
            ("BT /F1 9 Tf 70 540 Td ([EVIDENCE / SCREENSHOT PLACEHOLDER: Pull Request checks passed against upstream]) Tj ET", 0),
            ("BT /F2 13 Tf 50 490 Td (E. Candidate Declaration) Tj ET", 0),
            ("BT /F1 10 Tf 60 465 Td (\"I hereby declare that the submitted implementation has been completed by me. I have) Tj ET", 0),
            ("BT /F1 10 Tf 60 450 Td (tested the Docker configurations, Docker Compose deployment, Docker Hub image publishing) Tj ET", 0),
            ("BT /F1 10 Tf 60 435 Td (and GitHub Actions CI/CD pipeline. The screenshots and evidence included in this) Tj ET", 0),
            ("BT /F1 10 Tf 60 420 Td (document represent my actual implementation.\") Tj ET", 0),
            ("BT /F2 10 Tf 60 370 Td (Candidate Name: Bhavya Arora) Tj ET", 0),
            ("BT /F1 10 Tf 60 355 Td (Date:           November 18, 2026) Tj ET", 0),
            ("BT /F1 10 Tf 60 340 Td (Institution:    KIET Group of Institutions) Tj ET", 0),
            ("BT /F2 10 Tf 50 50 Td (Page 2 of 2 - Software Engineering & DevOps (AI310B)) Tj ET", 0)
        ]
    ]

    objects = []
    
    # 1: Catalog
    # 2: Pages
    # 3: Font Helvetica
    # 4: Font Helvetica-Bold
    # Page 1: 5 (Page), 6 (Contents)
    # Page 2: 7 (Page), 8 (Contents)
    
    font_reg = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
    font_bold = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"
    
    stream1 = "\n".join(cmd for cmd, _ in pages_text[0])
    stream2 = "\n".join(cmd for cmd, _ in pages_text[1])
    
    content1 = f"<< /Length {len(stream1)} >>\nstream\n{stream1}\nendstream"
    content2 = f"<< /Length {len(stream2)} >>\nstream\n{stream2}\nendstream"
    
    page1 = "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents 6 0 R >>"
    page2 = "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents 8 0 R >>"
    
    pages = "<< /Type /Pages /Kids [5 0 R 7 0 R] /Count 2 >>"
    catalog = "<< /Type /Catalog /Pages 2 0 R >>"
    
    all_objs = [
        catalog,   # 1
        pages,     # 2
        font_reg,  # 3
        font_bold, # 4
        page1,     # 5
        content1,  # 6
        page2,     # 7
        content2   # 8
    ]
    
    body = bytearray()
    body.extend(b"%PDF-1.4\n")
    
    offsets = []
    for i, obj in enumerate(all_objs, 1):
        offsets.append(len(body))
        body.extend(f"{i} 0 obj\n{obj}\nendobj\n".encode("latin1"))
        
    startxref = len(body)
    body.extend(f"xref\n0 {len(all_objs) + 1}\n0000000000 65535 f \n".encode("latin1"))
    for off in offsets:
        body.extend(f"{off:010d} 00000 n \n".encode("latin1"))
        
    body.extend(f"trailer\n<< /Size {len(all_objs) + 1} /Root 1 0 R >>\nstartxref\n{startxref}\n%%EOF\n".encode("latin1"))
    
    with open(filename, "wb") as f:
        f.write(body)
    print(f"PDF created successfully: {filename} ({len(body)} bytes)")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "ROLL_NUMBER_STUDENT_NAME_SET2.pdf"
    create_pdf(out)
