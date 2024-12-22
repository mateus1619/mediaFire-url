
# MediaFire-URL

This project allows you to get the direct download link for a file hosted on MediaFire. By providing the **file ID**, the application processes the information and returns the download link.
## Features

- Gets the file ID from MediaFire
- Generates the direct download link
- Simplifies the process of accessing files on MediaFire
## Documentation

Access the complete API documentation at the link below:

[Documentation](https://mediafire-url.vercel.app/)

This link takes you directly to the documentation interface, where you can see details on how to use the API, request examples, accepted parameters and much more.
## API Reference

#### Base URL

[`mediafire-url.vercel.app`](https://mediafire-url.vercel.app)

#### How to Find File ID in original Mediafire URL

To use the API correctly, you need to provide the **File ID**. The file ID can be found in the original Mediafire URL, between the `/file/` (or `/file_premium/`) part and the file name.

| Case              | URL example                                            | File ID         |
|-------------------|--------------------------------------------------------|-----------------|
| **with `/file_premium/`** | `<DOMAIN>/file_premium/<FILE_ID>/<FILE_NAME>/file` | `ol9s654lvkuyc1o` |
| **with `/file/`** | `<DOMAIN>/file/<FILE_ID>/<FILE_NAME>/file`        | `ol9s654lvkuyc1o` |
| **Simple URL (with `?`)** | `<DOMAIN>/?<file_id>` | `ol9s654lvkuyc1o` |


---

#### Endpoint: Get URL

```http
POST /api/media
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. media ID |

#### Request Example

```bash
curl \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"id": "ol9s654lvkuyc1o"}' \
  https://mediafire-url.vercel.app/api/media
```

#### Exemplo de Resposta

```json
{
  "name": "string",
  "link": "string"
}
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_URL`
`CONTACTS`
## Tech Stack

**Server:** Python, FastAPI, Uvicorn