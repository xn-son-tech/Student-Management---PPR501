from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class BaseResponse(Generic[T]): 
    def __init__(
        self, 
        data: Optional[List[T]] = None,
        page_size: int = 0,
        page_number: int = 0,
        error: Optional[List[str]] = None,
        success: bool = True
    ): 
        self.page_size = page_size
        self.page_number = page_number
        self.data = data or []
        self.error = error or []
        self.success = success

    def to_dict(self):
        return {
            "page_size": self.page_size,
            "page_number": self.page_number,
            "data": self.data,
            "error": self.error,
            "success": self.success
        }