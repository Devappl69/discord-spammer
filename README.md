# Discord Spammer (With Proxy Support)

### This python script automatically sends a custom message to a list of channels and through a list of proxies.

## Requirements

Requests, Random and Time. These modules can be installed with either PIP or Brew

## Usage

- Download the files (duh)
- Make sure they are all in the same folder, they are correctly named, and that there are no duplicates
- Add channel IDs to _channels.txt_ (each on a new line)
- Add proxies to _proxies.txt_ (each also on a new line)
- Change the value of “Authorization” in the headers to your discord token
- Change the value of message_content (use 3 quotation marks for multi line strings)
- Run the script

## Limitations

Sadly (depending on how you look at it), rate limits are a thing, so you won’t be able to endlessly send messages however fast you want. I have added proxy support, but for those who don't have any proxies (or not good ones) will probably face rate limits at one point or another. Below is some information on the Discord rate limits.

**Rate limits:**

- 10k requests every 10 minutes
- 50 requests per second
- Up to 1 hour of blocked requests when being rate limited

## Future updates for this project

There are several things that aren't perfect or have not been added entirely yet. Below are some features that I hope to add to this project in the near future.

- Support for several accounts at once
- Multiple messages / randomly choosing messages from a list
- Auto-joining accounts to the server in case they aren't already

## Disclaimer and License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This code is licensed under MIT. The full license is included in the _LICENSE_ file.
