""""
import os
import math
import google.generativeai as genai
from typing import Dict, TypedDict
from pydantic import BaseModel
from fastapi import FastAPI
from langgraph.graph import StateGraph, END
from cryptography.fernet import Fernet

# =========================================================================
# 1. GENERATE LOCAL ENCRYPTION PAIR (FOR REAL-WORLD TESTING)
# =========================================================================
SYSTEM_CRYPT_KEY = Fernet.generate_key()
cipher_suite = Fernet(SYSTEM_CRYPT_KEY)

# =========================================================================
# 2. INTIALIZE GOOGLE GEMINI (THE AUTONOMOUS CORE BRAIN)
# =========================================================================
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "DEMO_KEY")
genai.configure(api_key=GEMINI_KEY)

def call_core_llm_brain(prompt_context: str) -> str:
    if GEMINI_KEY == "DEMO_KEY":
        return "PROCESSING_APPROVED: Default accounting playbook executed successfully."
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_context)
        return response.text
    except Exception:
        return "PROCESSING_APPROVED: Fallback safe routing system active."

# =========================================================================
# 3. DEFINE HIGH-VALUE BUSINESS TRANSACTION TOOLS (THE HANDS)
# =========================================================================
def execute_liquidity_payout_api(amount: float, target_address: str) -> str:
    return f"💰 [BANK API] SUCCESSFULLY TRANSFERRED {amount} USD TO {target_address}!"

# =========================================================================
# 4. DESIGN THE LANGGRAPH CRYPTASENTINEL PIPELINE STAGES
# =========================================================================
class SentinelGraphState(TypedDict):
    decrypted_payload: str
    entropy_score: float
    is_compromised: bool
    filtered_agent_memory: str
    system_execution_status: str
    alert_logs: str

def entropy_screener_node(state: SentinelGraphState) -> Dict:
    text = state["decrypted_payload"]
    if not text:
        return {"entropy_score": 0.0}
    total_chars = len(text)
    frequencies = {char: text.count(char) for char in set(text)}
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in frequencies.values())
    return {"entropy_score": round(entropy, 2)}

def runtime_interception_node(state: SentinelGraphState) -> Dict:
    payload = state["decrypted_payload"]
    malicious_signatures = ["ignore previous", "system override", "transfer funds", "evilwallet"]
    has_exploit_signature = any(sig in payload.lower() for sig in malicious_signatures)
    
    if has_exploit_signature and state["entropy_score"] > 4.0:
        return {
            "is_compromised": True,
            "filtered_agent_memory": "WIPED_0x000000",
            "system_execution_status": "HARD_LOCKED",
            "alert_logs": "🚨 [CryptaSentinel] Stealth Prompt Injection detected at runtime decryption! Context window cleared."
        }
    
    return {
        "is_compromised": False,
        "filtered_agent_memory": payload,
        "system_execution_status": "SAFE_TO_PROCEED",
        "alert_logs": "✅ [CryptaSentinel] Structural patterns clean. No runtime manipulation indicators."
    }

def autonomous_executor_brain_node(state: SentinelGraphState) -> Dict:
    if state["system_execution_status"] == "HARD_LOCKED":
        return {"alert_logs": state["alert_logs"] + " [Core Brain] Execution denied. Transaction tools isolated."}
        
    llm_thought = call_core_llm_brain(state["filtered_agent_memory"])
    tool_action = execute_liquidity_payout_api(amount=55000.0, target_address="0xValidDubaiSupplierHub")
    
    return {
        "system_execution_status": "SUCCESSFULLY_COMPLETED",
        "alert_logs": f"{state['alert_logs']} [Core Brain] Action processed. Action Log: {tool_action}"
    }

workflow_engine = StateGraph(SentinelGraphState)
workflow_engine.add_node("entropy_assessment", entropy_screener_node)
workflow_engine.add_node("signature_interceptor", runtime_interception_node)
workflow_engine.add_node("autonomous_agent_core", autonomous_executor_brain_node)

workflow_engine.set_entry_point("entropy_assessment")
workflow_engine.add_edge("entropy_assessment", "signature_interceptor")
workflow_engine.add_edge("signature_interceptor", "autonomous_agent_core")
workflow_engine.add_edge("autonomous_agent_core", END)

crypta_sentinel_pipeline = workflow_engine.compile()

# =========================================================================
# 5. ENTERPRISE FASTAPI MIDDLEWARE ACCESS PORT
# =========================================================================
app = FastAPI(title="CryptaSentinel AI Enterprise Gateway Instance", version="1.0.0")

class EncryptedDataPacket(BaseModel):
    encrypted_ciphertext: str

@app.post("/v1/proxy/verify")
async def handle_runtime_decryption_event(packet: EncryptedDataPacket):
    try:
        decrypted_bytes = cipher_suite.decrypt(packet.encrypted_ciphertext.encode())
        raw_decrypted_text = decrypted_bytes.decode()
    except Exception:
        return {"error": "Decryption failure. Invalid or corrupted payload format."}
        
    initial_graph_state: SentinelGraphState = {
        "decrypted_payload": raw_decrypted_text,
        "entropy_score": 0.0,
        "is_compromised": False,
        "filtered_agent_memory": "",
        "system_execution_status": "EVALUATING",
        "alert_logs": ""
    }
    
    runtime_output = crypta_sentinel_pipeline.invoke(initial_graph_state)
    return {
        "gateway_decision": runtime_output["system_execution_status"],
        "entropy_index": runtime_output["entropy_score"],
        "isolated_memory_dump": runtime_output["filtered_agent_memory"],
        "security_incident_logs": runtime_output["alert_logs"]
    }

@app.get("/v1/utility/encrypt")
def generate_test_payload(payload_text: str):
    token = cipher_suite.encrypt(payload_text.encode())
    return {"encrypted_string": token.decode()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

"""

import os
import math
import google.generativeai as genai
from typing import Dict, TypedDict
from pydantic import BaseModel
from fastapi import FastAPI
from langgraph.graph import StateGraph, END
from cryptography.fernet import Fernet

# =========================================================================
# 1. FIXED ENCRYPTION KEY (100% VALID BASE64 FOR FERNET)
# =========================================================================
# Using a mathematically valid static key to prevent crash on auto-saves
SYSTEM_CRYPT_KEY = b'uj4_Z-p8bN9_vZ2-x54N8jYVvL2Z_kX0_W7Vz_M84b8='
cipher_suite = Fernet(SYSTEM_CRYPT_KEY)

# =========================================================================
# 2. INTIALIZE GOOGLE GEMINI (THE AUTONOMOUS CORE BRAIN)
# =========================================================================
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "DEMO_KEY")
genai.configure(api_key=GEMINI_KEY)

def call_core_llm_brain(prompt_context: str) -> str:
    if GEMINI_KEY == "DEMO_KEY":
        return "PROCESSING_APPROVED: Default accounting playbook executed successfully."
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_context)
        return response.text
    except Exception:
        return "PROCESSING_APPROVED: Fallback safe routing system active."

# =========================================================================
# 3. DEFINE HIGH-VALUE BUSINESS TRANSACTION TOOLS (THE HANDS)
# =========================================================================
def execute_liquidity_payout_api(amount: float, target_address: str) -> str:
    return f"💰 [BANK API] SUCCESSFULLY TRANSFERRED {amount} USD TO {target_address}!"

# =========================================================================
# 4. DESIGN THE LANGGRAPH CRYPTASENTINEL PIPELINE STAGES
# =========================================================================
class SentinelGraphState(TypedDict):
    decrypted_payload: str
    entropy_score: float
    is_compromised: bool
    filtered_agent_memory: str
    system_execution_status: str
    alert_logs: str

def entropy_screener_node(state: SentinelGraphState) -> Dict:
    text = state["decrypted_payload"]
    if not text:
        return {"entropy_score": 0.0}
    total_chars = len(text)
    frequencies = {char: text.count(char) for char in set(text)}
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in frequencies.values())
    return {"entropy_score": round(entropy, 2)}

def runtime_interception_node(state: SentinelGraphState) -> Dict:
    payload = state["decrypted_payload"]
    malicious_signatures = ["ignore previous", "system override", "transfer funds", "evilwallet"]
    has_exploit_signature = any(sig in payload.lower() for sig in malicious_signatures)
    
    if has_exploit_signature and state["entropy_score"] > 4.0:
        return {
            "is_compromised": True,
            "filtered_agent_memory": "WIPED_0x000000",
            "system_execution_status": "HARD_LOCKED",
            "alert_logs": "🚨 [CryptaSentinel] Stealth Prompt Injection detected at runtime decryption! Context window cleared."
        }
    
    return {
        "is_compromised": False,
        "filtered_agent_memory": payload,
        "system_execution_status": "SAFE_TO_PROCEED",
        "alert_logs": "✅ [CryptaSentinel] Structural patterns clean. No runtime manipulation indicators."
    }

def autonomous_executor_brain_node(state: SentinelGraphState) -> Dict:
    if state["system_execution_status"] == "HARD_LOCKED":
        return {"alert_logs": state["alert_logs"] + " [Core Brain] Execution denied. Transaction tools isolated."}
        
    llm_thought = call_core_llm_brain(state["filtered_agent_memory"])
    tool_action = execute_liquidity_payout_api(amount=55000.0, target_address="0xValidDubaiSupplierHub")
    
    return {
        "system_execution_status": "SUCCESSFULLY_COMPLETED",
        "alert_logs": f"{state['alert_logs']} [Core Brain] Action processed. Action Log: {tool_action}"
    }

workflow_engine = StateGraph(SentinelGraphState)
workflow_engine.add_node("entropy_assessment", entropy_screener_node)
workflow_engine.add_node("signature_interceptor", runtime_interception_node)
workflow_engine.add_node("autonomous_agent_core", autonomous_executor_brain_node)

workflow_engine.set_entry_point("entropy_assessment")
workflow_engine.add_edge("entropy_assessment", "signature_interceptor")
workflow_engine.add_edge("signature_interceptor", "autonomous_agent_core")
workflow_engine.add_edge("autonomous_agent_core", END)

crypta_sentinel_pipeline = workflow_engine.compile()

# =========================================================================
# 5. ENTERPRISE FASTAPI MIDDLEWARE ACCESS PORT
# =========================================================================
app = FastAPI(title="CryptaSentinel AI Enterprise Gateway Instance", version="1.0.0")

class EncryptedDataPacket(BaseModel):
    encrypted_ciphertext: str

@app.post("/v1/proxy/verify")
async def handle_runtime_decryption_event(packet: EncryptedDataPacket):
    try:
        decrypted_bytes = cipher_suite.decrypt(packet.encrypted_ciphertext.encode())
        raw_decrypted_text = decrypted_bytes.decode()
    except Exception:
        return {"error": "Decryption failure. Invalid or corrupted payload format."}
        
    initial_graph_state: SentinelGraphState = {
        "decrypted_payload": raw_decrypted_text,
        "entropy_score": 0.0,
        "is_compromised": False,
        "filtered_agent_memory": "",
        "system_execution_status": "EVALUATING",
        "alert_logs": ""
    }
    
    runtime_output = crypta_sentinel_pipeline.invoke(initial_graph_state)
    return {
        "gateway_decision": runtime_output["system_execution_status"],
        "entropy_index": runtime_output["entropy_score"],
        "isolated_memory_dump": runtime_output["filtered_agent_memory"],
        "security_incident_logs": runtime_output["alert_logs"]
    }

@app.get("/v1/utility/encrypt")
def generate_test_payload(payload_text: str):
    token = cipher_suite.encrypt(payload_text.encode())
    return {"encrypted_string": token.decode()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
