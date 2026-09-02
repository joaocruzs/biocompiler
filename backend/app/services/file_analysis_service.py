from fastapi import HTTPException

from app.core.constants import MAX_FILE_SIZE

from app.services.file_service import (
    read_sequences_from_file
)

from app.services.batch_analyzer import (
    analyze_sequences
)

from app.services.report_service import (
    generate_summary
)


def process_uploaded_file(
    filename: str,
    content: bytes
) -> dict:
    """
    Processa um arquivo TXT contendo
    sequências de DNA.
    """

    if not filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Apenas arquivos .txt são permitidos."
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Arquivo excede o tamanho máximo permitido."
        )

    try:
        text_content = content.decode("utf-8")

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Erro ao ler o arquivo. Utilize UTF-8."
        )

    sequences = read_sequences_from_file(
        text_content
    )

    if not sequences:
        raise HTTPException(
            status_code=400,
            detail="O arquivo não possui sequências para análise."
        )

    results = analyze_sequences(
        sequences
    )

    summary = generate_summary(
        results
    )

    return {
        "total_sequences": len(results),
        "results": results,
        "summary": summary
    }