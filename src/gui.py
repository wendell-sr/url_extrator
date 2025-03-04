import tkinter as tk
from tkinter import ttk, messagebox
from src import extractor

class URLExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Extractor")
        
        self.url_label = ttk.Label(root, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.extract_button = ttk.Button(root, text="Extract URLs", command=self.extract_urls)
        self.extract_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.result_text = tk.Text(root, wrap="word", width=80, height=20)
        self.result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
    def extract_urls(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        result = extractor.extract_urls(url)
        if "error" in result:
            messagebox.showerror("Error", result["error"])
            return
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Internal Links:\n")
        for link in result["internal_links"]:
            self.result_text.insert(tk.END, link + "\n")
        
        self.result_text.insert(tk.END, "\nExternal Links:\n")
        for link in result["external_links"]:
            self.result_text.insert(tk.END, link + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLExtractorApp(root)
    root.mainloop()
