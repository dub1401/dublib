from enum import Enum

#==========================================================================================#
# >>>>> ПЕРЕЧИСЛЕНИЯ <<<<< #
#==========================================================================================#

class Protocol(Enum):
	"""Protocol type."""

	SOCKS4 = "socks4"
	SOCKS5 = "socks5"
	HTTPS = "https"
	HTTP = "http"
	SFTP = "sftp"
	FTP = "ftp"

class RequestType(Enum):
	"""Supported request type."""

	DELETE = "delete"
	GET = "get"
	POST = "post"

class WebLib(Enum):
	"""Supported requests lib."""

	curl_cffi = "curl_cffi"
	requests = "requests"
	httpx = "httpx"

