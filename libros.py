# Campo y ID para eliminar libro
        e_id_eliminar = ctk.CTkEntry(frame_form, placeholder_text="ID a eliminar", width=100, corner_radius=10)
        e_id_eliminar.grid(row=0, column=3, padx=8, pady=15)

        def eliminar_libro():
            id_del = e_id_eliminar.get().strip()
            if not id_del:
                messagebox.showwarning("Validación", "Ingresa el ID del libro que deseas eliminar.")
                return
            
            exito = lista_libros.eliminar_por_id_libro(id_del)
            if exito:
                messagebox.showinfo("Éxito", f"Libro con ID '{id_del}' eliminado correctamente.")
                self.vista_libros()
            else:
                messagebox.showerror("Error", f"No se encontró ningún libro con el ID '{id_del}'.")

        btn_del = ctk.CTkButton(
            frame_form, text="🗑️", fg_color="#FF6B6B", 
            hover_color="#FF5252", text_color="#FFFFFF", 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=10, width=45, command=eliminar_libro
        )
        btn_del.grid(row=0, column=6, padx=4, pady=15)
