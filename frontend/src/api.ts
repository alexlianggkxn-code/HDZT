const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export interface ContactPayload {
  name: string;
  organization: string;
  contact: string;
  interest: string;
  message: string;
}

export interface ContactResponse {
  id: number;
  message: string;
}

export async function submitContactLead(payload: ContactPayload): Promise<ContactResponse> {
  const response = await fetch(`${API_BASE_URL}/api/contact/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Contact request failed");
  }

  return response.json();
}
