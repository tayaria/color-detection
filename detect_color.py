import cv2
import numpy as np

def detect_color(frame):
    """
    Détecte la couleur dominante dans l'image et retourne le nom de la couleur.
    """
    # Convertir l'image de BGR à HSV (plus facile pour la détection de couleur)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Définir les plages de couleurs en HSV
    
    # Rouge (deux plages car le rouge s'étend sur 0° et 180°)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    
    # Vert
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    # Bleu
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Jaune
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Créer les masques pour chaque couleur
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Compter le nombre de pixels non-nuls pour chaque couleur
    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)
    yellow_pixels = cv2.countNonZero(mask_yellow)
    
    # Déterminer la couleur dominante
    colors = {
        "ROUGE": red_pixels,
        "VERT": green_pixels,
        "BLEU": blue_pixels,
        "JAUNE": yellow_pixels
    }
    
    # Seuil minimum pour déclarer une couleur détectée
    threshold = 500
    
    # Trouver la couleur avec le plus de pixels (si au-dessus du seuil)
    detected_color = None
    max_pixels = 0
    
    for color_name, pixel_count in colors.items():
        if pixel_count > max_pixels and pixel_count > threshold:
            max_pixels = pixel_count
            detected_color = color_name
    
    return detected_color, colors

def main():
    # Initialiser la caméra
    cap = cv2.VideoCapture(0)
    
    # Vérifier si la caméra s'est ouverte correctement
    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la caméra.")
        return
    
    print("Détecteur de couleurs")
    print("Appuyez sur 'q' pour quitter")
    print("Placez un objet coloré devant la caméra")
    
    while True:
        # Capturer une image de la caméra
        ret, frame = cap.read()
        
        if not ret:
            print("Erreur: Impossible de lire l'image de la caméra.")
            break
        
        # Redimensionner l'image pour un traitement plus rapide
        frame = cv2.resize(frame, (640, 480))
        
        # Détecter la couleur dominante
        detected_color, color_counts = detect_color(frame)
        
        # Afficher le résultat sur l'image
        if detected_color:
            # Afficher le message avec la couleur détectée
            if detected_color == "ROUGE":
                message = "Couleur est ROUGE"
                text_color = (0, 0, 255)  # Rouge en BGR
            elif detected_color == "VERT":
                message = "Couleur est VERT"
                text_color = (0, 255, 0)  # Vert en BGR
            elif detected_color == "BLEU":
                message = "Couleur est BLEU"
                text_color = (255, 0, 0)  # Bleu en BGR
            elif detected_color == "JAUNE":
                message = "Couleur est JAUNE"
                text_color = (0, 255, 255)  # Jaune en BGR
            else:
                message = "Couleur non reconnue"
                text_color = (255, 255, 255)  # Blanc
            
            # Dessiner un rectangle de fond pour le texte
            cv2.rectangle(frame, (10, 10), (400, 80), (0, 0, 0), -1)
            
            # Afficher le message
            cv2.putText(frame, message, (20, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.2, text_color, 2)
        else:
            # Aucune couleur détectée au-dessus du seuil
            cv2.rectangle(frame, (10, 10), (400, 80), (0, 0, 0), -1)
            cv2.putText(frame, "Aucune couleur detectee", (20, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Afficher les compteurs de pixels pour le débogage
        y_offset = 100
        for color_name, pixel_count in color_counts.items():
            text = f"{color_name}: {pixel_count} pixels"
            cv2.putText(frame, text, (20, y_offset), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            y_offset += 30
        
        # Afficher l'image
        cv2.imshow('Detecteur de couleurs', frame)
        
        # Quitter avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libérer la caméra et fermer les fenêtres
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()