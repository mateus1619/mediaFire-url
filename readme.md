
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

#### Endpoint: Get URL

```http
POST /api/media
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. media ID |

#### Request Example

```curl
curl -X POST https://mediafire-url.vercel.app/api/media
-H "Content-Type: application/json"
-d '{"id": "xxx2321xxx"}'
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