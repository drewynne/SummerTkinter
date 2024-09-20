""" Show a toast notification with a custom dialog """
        # Create a Toplevel window
        toast = Toplevel(self.root)
        toast.title(title)
        toast.geometry("300x100")

        # Add a Label with the message
        Label(toast, text=message).pack(expand=True)

        # Automatically close the toast after the specified duration
        toast.after(duration, toast.destroy)